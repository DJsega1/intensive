from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {"about1": "Меня зовут Никита, Мне 17, я живу в городе Саранск. \
                        Учусь в Лицее МГУ им. Н. П. Огарёва в 11 классе. Имею много хобби, \
                        но могу выделить самые любимые: баскетбол, компьютерные игры, программирование.",
                   "about2": "Обучался в Лицее Академии Яндекса 2 года, где получил навыки программирования. \
                        Мой основной ЯП - Python. Понимаю основные принципы ООП. \
                        Работал с библиотеками Flask, sqlalchemy, pillow, iogram и др. Имею базовые представления об \
                        устройстве сети и веб-разработке в целом.",
                   "telegram": "https://t.me/djsega1",
                   "mail": "djsega1@yandex.ru",
                   }
        return context
