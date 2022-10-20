output_a = "{:d}".format(52) # 문자열처리가 아닌 정수 처리
output_b = "{:5d}".format(52) # 총 5칸을 차지하고 오른쪽에서 왼쪽으로 
output_c = "{:05d}".format(52) # 총 5칸 차지하고 왼쪽에 남은 공간 0으로 채우기
output_d = "{:05d}".format(-52) # 맨 앞칸은 -부호가 차지한다. -0052
output_e = "{:+d}".format(52) # 부호화 함께 출력 +52
output_f = "{:+d}".format(-52) # 부호화 함께 출력 -52
output_g = "{: d}".format(52) # 부호부분 공백 ,, 즉, 총 3칸 차지하고 맨 앞 공백
output_h = "{: d}".format(-52) # -52 출력
output_i = "{:+5d}".format(52) # 기호 뒤로 밀기 즉, 앞 2칸 공백 이후 +52
output_j = "{:=+5d}".format(52) # 기호 앞으로 밀기, 부호만 맨 앞으로

# 부동 소수점 출력
output_k = "{:f}".format(52.273) 
output_l = "{:15f}".format(52.273) # 15차지 오른쪽에서 왼쪽으로 .도 1칸차지 
output_m = "{:15.2f}".format(52.273) # 15칸차지 2칸은 소수점

output_n = 52.0
output_o = "{:g}".format(output_n) # 의미없는 소수점 제거 => 52 s