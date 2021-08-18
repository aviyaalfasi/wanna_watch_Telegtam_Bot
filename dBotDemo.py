from telegram.ext import CommandHandler, CallbackQueryHandler, Updater
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import YouTubeConnector
import MoviesDB


class TelegramBotWrapper:
    result: list = []
    result2: list = []

    ############################### Bot ############################################
    @classmethod
    def start(cls, update, context):
        TelegramBotWrapper.result.clear()
        TelegramBotWrapper.result2.clear()
        update.message.reply_text(text="""\
    Hi there, I am WannaWatch Bot!
    
    Welcome to the incredible Bot, which will help you decide what movie you want!. 
    based on your mood, or the genre - you will get all the details you need to pick a movie.
    
    So, just choose!
                                        """, reply_markup=TelegramBotWrapper.type_choose_keyboard())

    @classmethod
    def type_choose(cls, update, context):
        TelegramBotWrapper.result.clear()
        TelegramBotWrapper.result2.clear()
        query = update.callback_query
        query.answer()
        query.edit_message_text(text=""""\
    Hi there, I am WannaWatch Bot!
    
    Welcome to the incredible Bot, which will help you decide what movie you want!. 
    based on your mood, or the genre - you will get all the details you need to pick a movie.
    
    So, just choose!
                                        """,
                                reply_markup=TelegramBotWrapper.type_choose_keyboard())

    @classmethod
    def genre(cls, update, context):
        query = update.callback_query
        query.answer()
        query.edit_message_text(text="Please Pick a Genre", reply_markup=TelegramBotWrapper.genre_keyboard())

    @classmethod
    def situation(cls, update, context):
        query = update.callback_query
        query.answer()
        query.edit_message_text(text="Please Pick a Situation", reply_markup=TelegramBotWrapper.situation_keyboard())

    @classmethod
    def action_genre(cls, update, context):
        query = update.callback_query
        query.answer()
        query.edit_message_text(text="The action Movies", reply_markup=TelegramBotWrapper.action_genre_keyboard())

    @classmethod
    def drama_genre(cls, update, context):
        query = update.callback_query
        query.answer()
        query.edit_message_text(text="The action Movies", reply_markup=TelegramBotWrapper.drama_genre_keyboard())

    @classmethod
    def friends_situation(cls, update, context):
        query = update.callback_query
        query.answer()
        query.edit_message_text(text="Watch With Friends", reply_markup=TelegramBotWrapper.friends_situation_keyboard())

    @classmethod
    def family_situation(cls, update, context):
        query = update.callback_query
        query.answer()
        query.edit_message_text(text="Watch With Family", reply_markup=TelegramBotWrapper.family_situation_keyboard())

    """def date_situation(update, context):
        query = update.callback_query
        query.answer()
        query.edit_message_text(text="Watch In Date", reply_markup=date_situation_keyboard())"""

    @classmethod
    def myself_situation(cls, update, context):
        query = update.callback_query
        query.answer()
        query.edit_message_text(text="Whatch With Yourself",
                                reply_markup=TelegramBotWrapper.myself_situation_keyboard())

    ############################### KeyBoards ############################################
    @classmethod
    def type_choose_keyboard(cls):
        keyboard = [
            [InlineKeyboardButton("Movie By Genre", callback_data='movie_by_genre')],
            [InlineKeyboardButton("Movie by Situation", callback_data='movie_by_situation')]
        ]
        return InlineKeyboardMarkup(keyboard)

    @classmethod
    def genre_keyboard(cls):
        keyboard = [
            [InlineKeyboardButton("Action", callback_data='action_g')],
            [InlineKeyboardButton("Adventure", callback_data='adventure')],
            [InlineKeyboardButton("Animation", callback_data='animation')],
            [InlineKeyboardButton("Biography", callback_data='biography')],
            [InlineKeyboardButton("Crime", callback_data='crime')],
            [InlineKeyboardButton("Comedy", callback_data='comedy')],
            [InlineKeyboardButton("Drama", callback_data='drama_g')],
            [InlineKeyboardButton("Fantasy", callback_data='fantasy')],
            [InlineKeyboardButton("Family", callback_data='family')],
            [InlineKeyboardButton("History", callback_data='history')],
            [InlineKeyboardButton("Horror", callback_data='horror')],
            [InlineKeyboardButton("Music", callback_data='music')],
            [InlineKeyboardButton("Musical", callback_data='musical')],
            [InlineKeyboardButton("Romance", callback_data='romance')],
            [InlineKeyboardButton("Sci-Fi", callback_data='scifi')],
            [InlineKeyboardButton("Western", callback_data='western')],
            [InlineKeyboardButton("War", callback_data='war')],
            [InlineKeyboardButton('Go Back - Type of Watching', callback_data='type')],
            # [InlineKeyboardButton('Next - Find Movie', callback_data='find_movie')]
        ]
        return InlineKeyboardMarkup(keyboard)

    @classmethod
    def situation_keyboard(cls):
        keyboard = [
            [InlineKeyboardButton("With Family", callback_data='w_family')],
            [InlineKeyboardButton("With Friends", callback_data='w_friends')],
            # [InlineKeyboardButton("With Date", callback_data='w_date')],
            [InlineKeyboardButton("With MySelf", callback_data='w_myself')],
            [InlineKeyboardButton('Go Back - Type of Watching', callback_data='type')]
        ]
        return InlineKeyboardMarkup(keyboard)

    @classmethod
    def action_genre_keyboard(cls):
        res = MoviesDB.MoviesDBWrapper.movies_by_genre(['Action'])  # list of all the drama movies
        for movie in res:
            content = "Movie: " + movie.title + " | Rating: " + str(movie.rating)
            TelegramBotWrapper.result2.append([InlineKeyboardButton(text=content,
                                                                    url=YouTubeConnector.YouTubeConnectorWrapper.get_trailer_url(
                                                                        movie))])
        TelegramBotWrapper.result2.append([InlineKeyboardButton('Go Back - Type of Watching', callback_data='type')])
        return InlineKeyboardMarkup(TelegramBotWrapper.result2)

    @classmethod
    def drama_genre_keyboard(cls):
        res = MoviesDB.MoviesDBWrapper.movies_by_genre(['Drama'])  # list of all the drama movies
        for movie in res:
            content = "Movie: " + movie.title + " | Rating: " + str(movie.rating)
            TelegramBotWrapper.result2.append([InlineKeyboardButton(text=content,
                                                                    url=YouTubeConnector.YouTubeConnectorWrapper.get_trailer_url(
                                                                        movie))])
        TelegramBotWrapper.result2.append([InlineKeyboardButton('Go Back - Type of Watching', callback_data='type')])
        return InlineKeyboardMarkup(TelegramBotWrapper.result2)

    ####################Situation Keyboard#############################
    @classmethod
    def friends_situation_keyboard(cls):
        res = MoviesDB.MoviesDBWrapper.movies_by_situations("Friends")
        for movie in res:
            content = "Movie: " + movie.title + " | Rating: " + str(movie.rating)
            TelegramBotWrapper.result.append([InlineKeyboardButton(text=content,
                                                                   url=YouTubeConnector.YouTubeConnectorWrapper.get_trailer_url(
                                                                       movie))])
        TelegramBotWrapper.result.append([InlineKeyboardButton('Go Back - Type of Watching', callback_data='type')])
        return InlineKeyboardMarkup(TelegramBotWrapper.result)

    """
    def date_situation_keyboard():
        res = MoviesDB.MoviesDBWrapper.movies_by_situations("Date")
        for movie in res:
            content = "Movie: " + movie.title + " | Rating: "+  str(movie.rating)
            result.append([InlineKeyboardButton(text = content,
                                                 url=YouTubeConnector.YouTubeConnectorWrapper.get_trailer_url(movie))])
        result.append([InlineKeyboardButton('Go Back - Type of Watching', callback_data='type')])
        return InlineKeyboardMarkup(result)"""

    @classmethod
    def family_situation_keyboard(cls):
        res = MoviesDB.MoviesDBWrapper.movies_by_situations("Family")
        for movie in res:
            content = "Movie: " + movie.title + " | Rating: " + str(movie.rating)
            TelegramBotWrapper.result.append([InlineKeyboardButton(text=content,
                                                                   url=YouTubeConnector.YouTubeConnectorWrapper.get_trailer_url(
                                                                       movie))])
        TelegramBotWrapper.result.append([InlineKeyboardButton('Go Back - Type of Watching', callback_data='type')])
        return InlineKeyboardMarkup(TelegramBotWrapper.result)

    @classmethod
    def myself_situation_keyboard(cls):
        res = MoviesDB.MoviesDBWrapper.movies_by_situations("Myself & I")
        for movie in res:
            content = "Movie: " + movie.title + " | Rating: " + str(movie.rating)
            TelegramBotWrapper.result.append([InlineKeyboardButton(text=content,
                                                                   url=YouTubeConnector.YouTubeConnectorWrapper.get_trailer_url(
                                                                       movie))])
        TelegramBotWrapper.result.append([InlineKeyboardButton('Go Back - Type of Watching', callback_data='type')])
        return InlineKeyboardMarkup(TelegramBotWrapper.result)

    @classmethod
    def handlers(cls):
        updater = Updater('1996155625:AAEck7pMRNA-HBy2h03n5ep3tkf-mRoztLk', use_context=True)

        updater.dispatcher.add_handler(CommandHandler('start', TelegramBotWrapper.start))
        updater.dispatcher.add_handler(CallbackQueryHandler(TelegramBotWrapper.type_choose, pattern='type'))
        updater.dispatcher.add_handler(CallbackQueryHandler(TelegramBotWrapper.genre, pattern='movie_by_genre'))
        updater.dispatcher.add_handler(CallbackQueryHandler(TelegramBotWrapper.situation, pattern='movie_by_situation'))
        updater.dispatcher.add_handler(CallbackQueryHandler(TelegramBotWrapper.action_genre, pattern="action_g"))
        updater.dispatcher.add_handler(CallbackQueryHandler(TelegramBotWrapper.drama_genre, pattern="drama_g"))
        updater.dispatcher.add_handler(CallbackQueryHandler(TelegramBotWrapper.friends_situation, pattern="w_friends"))
        updater.dispatcher.add_handler(CallbackQueryHandler(TelegramBotWrapper.family_situation, pattern="w_family"))
        # updater.dispatcher.add_handler(CallbackQueryHandler(date_situation, pattern="w_date"))
        updater.dispatcher.add_handler(CallbackQueryHandler(TelegramBotWrapper.myself_situation, pattern="w_myself"))
        updater.start_polling()
