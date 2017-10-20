from object_test import Systerm, Spider

sys = Systerm()
sys.Login()
sys.init_Spider()
spider = Spider()
print(spider.session_stat)
print(spider.session_custserv)