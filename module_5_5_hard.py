from time import sleep
from multipledispatch import dispatch

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age
    def __str__(self):
        return self.nickname

class Video:
    def __init__(self, title, duration, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self. adult_mode = adult_mode
class UrTube:
    def __init__(self):
        self.users = {}
        self.videos = {}
        self.current_user = None

    @dispatch()
    def __contains__(self, video_:Video):
        if self.videos.get(video_.title):
            return True
        else:
            return False

    @dispatch()
    def __contains__(self, user_: User):
        if self.users.get(user_.nickname):
            return True
        else:
            return False

    def log_in(self, nickname, password):
        checking_user = self.users.get(nickname)
        if checking_user and checking_user.password ==  hash(password):
            current_user = checking_user
        else:
            print('Пользователь не найден. Проверьте правильность имени или зарегистрируйтесь.')
    def register(self,nickname, password, age):
        if self.users.get(nickname):
            print(f'Пользователь {nickname} уже существует')
        else:
            self.current_user = User(nickname, password, age)
            self.users[nickname] = self.current_user

    def log_out(self):
        self.current_user = None
    def add(self, *args: Video):
        for video_ in args:
            if not video_ in self:
                self.videos[video_.title] = video_
    def get_videos(self, search_word:str):
        ucase_search_word = search_word.upper()
        founded_titles = []
        for self_video_title in self.videos.keys():
            if ucase_search_word in self_video_title.upper():
                founded_titles.append(self_video_title)
        return founded_titles
    def watch_video(self, title):
        if self.current_user == None:
            print('Войдите в аккаунт, чтобы смотреть видео')
        else:
            watching_video = self.videos.get(title)
            if watching_video:
                    if watching_video.adult_mode and self.current_user.age < 18:
                        print('Вам нет 18 лет, пожалуйста покиньте страницу')
                    else:
                        while watching_video.time_now < watching_video.duration:
                            sleep(1)
                            watching_video.time_now += 1
                            print(watching_video.time_now, end = ' ')
                        print('Конец видео')
                        watching_video.time_now = 0

if __name__ == "__main__":
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    # Добавление видео
    ur.add(v1, v2)

    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')

    # Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)

    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')