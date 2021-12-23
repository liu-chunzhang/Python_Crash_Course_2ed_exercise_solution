# 5.4(1)的要求：检查外星人是否是绿色的，是就打印一条消息，指出玩家因射杀该外星人获得了5分。
# 5.4(2)的要求：若外星人不是绿色的，就打印一条消息，指出玩家获得了10分。
# 5.4(3)的要求：执行else代码块版本。
alien_color = 'green'

if alien_color == 'green' :
	scores = 5
else :
	scores = 10

print(f"You get {scores} points.")