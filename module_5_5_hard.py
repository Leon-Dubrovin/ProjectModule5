from time import sleep

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
        self.users = []
        self.videos = []
        self.current_user = None
    def __contains__(self, video_:Video):
        for self_video in self.videos:
            if video_.title == self_video.title:
                return True
        return False
    def log_in(self, nickname, password):
        for user_ in self.users:
            if user_.nickname == nickname and user_.password == hash(password):
                current_user = user_
                #print(f'Добро пожаловать, {nickname}.')
                return
        print('Пользователь не найден. Проверьте правильность имени или зарегистрируйтесь.')
        return
    def register(self,nickname, password, age):
        for user_ in self.users:
            if user_.nickname == nickname:
                print(f'Пользователь {nickname} уже существует')
                return
        self.current_user = User(nickname, password, age)
        self.users.append(self.current_user)
        #print(f'Добро пожаловать, {nickname}.')
        return
    def log_out(self):
        self.current_user = None
    def add(self, *args: Video):
        for video_ in args:
            if not video_ in self:
                self.videos.append(video_)
        return
    def get_videos(self, search_word:str):
        UCase_search_word = search_word.upper()
        founded_titles = []
        for self_video in self.videos:
            if UCase_search_word in self_video.title.upper():
                founded_titles.append(self_video.title)
        return founded_titles
    def watch_video(self, title):
        if self.current_user == None:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return
        for self_video in self.videos:
            if title == self_video.title:
                if self_video.adult_mode and self.current_user.age < 18:
                    print('Вам нет 18 лет, пожалуйста покиньте страницу')
                    return
                while self_video.time_now < self_video.duration:
                    sleep(0)
                    self_video.time_now += 1
                    print(self_video.time_now, end = ' ')
                print('Конец видео')
                self_video.time_now = 0
                return

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