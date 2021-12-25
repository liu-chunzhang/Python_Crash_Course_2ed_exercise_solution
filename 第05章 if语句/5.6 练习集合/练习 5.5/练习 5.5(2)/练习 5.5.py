# 5.5(1)的要求：检查外星人是否是绿色的，是就打印一条消息，指出玩家因射杀该外星人获得了5分。
# 5.5(2)的要求：检查外星人是否是绿色的，是就打印一条消息，指出玩家因射杀该外星人获得了10分。
# 5.5(3)的要求：检查外星人是否是绿色的，是就打印一条消息，指出玩家因射杀该外星人获得了15分。
# 5.5(4)的要求：执行if-elif-else代码块的外星人是黄色的版本，其他颜色的放在并行版本中。
alien_color = 'yellow'

if alien_color == 'green' :
	scores = 5
elif alien_color == 'yellow' :
	scores = 10
else :
	scores = 15

print(f"You get {scores} points.")