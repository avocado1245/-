#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
[AI와 함께하는 교통문제 해결을 위한 데이터 분석 공모전]
팀 SSY 공식 분석 파이프라인 단일 실행 엔트리포인트 (run_all.py)

실행:
    python run_all.py
"""

import os
import sys
import subprocess

def main():
    print("=" * 80)
    print("🚀 [팀 SSY] 서울시 대중교통 사각지대(ART) 재진단 및 정류장 3등급 재배치 파이프라인")
    print("=" * 80)
    
    # 1. 메인 파이프라인 실행
    script_path = "code/master_pipeline.py" if os.path.exists("code/master_pipeline.py") else "master_pipeline.py"
    if not os.path.exists(script_path):
        print(f"❌ '{script_path}' 스크립트를 찾을 수 없습니다.")
        sys.exit(1)
        
    print(f"
[Step 1/2] 마스터 파이프라인 실행 중 ({script_path})...")
    ret = subprocess.run([sys.executable, script_path])
    if ret.returncode != 0:
        print("❌ 파이프라인 실행 중 오류가 발생했습니다.")
        sys.exit(ret.returncode)
        
    # 2. 결과 검산 테스트 실행
    test_path = "tests/test_pipeline.py" if os.path.exists("tests/test_pipeline.py") else "test_pipeline.py"
    if os.path.exists(test_path):
        print(f"
[Step 2/2] 데이터 정합성 및 통계 검증 테스트 실행 중 ({test_path})...")
        test_ret = subprocess.run([sys.executable, test_path])
        if test_ret.returncode != 0:
            print("⚠️ 검증 테스트에서 불일치가 발견되었습니다.")
            sys.exit(test_ret.returncode)
            
    print("
" + "=" * 80)
    print("🎉 전 과정 파이프라인 실행 및 검증 완료! 산출물 위치: ./output/")
    print("=" * 80)

if __name__ == "__main__":
    main()