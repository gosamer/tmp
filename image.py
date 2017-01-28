from captcha_solver import CaptchaSolver

solver = CaptchaSolver('browser')
with open(r"C:\Users\Gossamer\Desktop\Arbeit\captchas\captcha1.jpg", 'rb') as inp:
    raw_data = inp.read()
print(solver.solve_captcha(raw_data))