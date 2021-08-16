from telegram.ext import CommandHandler, CallbackQueryHandler, Updater
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import YouTubeConnector
import MoviesDB

Movies = ["Dear John", "Mama Mia"]
result = []
result2 = []



############################### Bot ############################################
def start(update, context):
    result.clear()
    result2.clear()
    update.message.reply_text(text="""\
Hi there, I am WannaWatch Bot!

Welcome to the incredible Bot, which will help you decide what movie you want!. 
based on your mood, or the genre - you will get all the details you need to pick a movie.

So, just choose!
                                    """, reply_markup=type_choose_keyboard())


def type_choose(update, context):
    result.clear()
    result2.clear()
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=""""\
Hi there, I am WannaWatch Bot!

Welcome to the incredible Bot, which will help you decide what movie you want!. 
based on your mood, or the genre - you will get all the details you need to pick a movie.

So, just choose!
                                    """,
                            reply_markup=type_choose_keyboard())


def genre(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text="Please Pick a Genre", reply_markup=genre_keyboard())


def situation(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text="Please Pick a Situation", reply_markup=situation_keyboard())


def action_genre(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text="The action Movies", reply_markup=action_genre_keyboard())

def drama_genre(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text="The action Movies", reply_markup=drama_genre_keyboard())

def friends_situation(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text="Watch With Friends", reply_markup=friends_situation_keyboard())

def family_situation(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text="Watch With Family", reply_markup=family_situation_keyboard())

"""def date_situation(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text="Watch In Date", reply_markup=date_situation_keyboard())"""

def myself_situation(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text="Whatch With Yourself", reply_markup=myself_situation_keyboard())
############################### KeyBoards ############################################
def type_choose_keyboard():
    keyboard = [
        [InlineKeyboardButton("Movie By Genre", callback_data='movie_by_genre')],
        [InlineKeyboardButton("Movie by Situation", callback_data='movie_by_situation')]
    ]
    return InlineKeyboardMarkup(keyboard)


def genre_keyboard():
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


def situation_keyboard():
    keyboard = [
        [InlineKeyboardButton("With Family", callback_data='w_family')],
        [InlineKeyboardButton("With Friends", callback_data='w_friends')],
        #[InlineKeyboardButton("With Date", callback_data='w_date')],
        [InlineKeyboardButton("With MySelf", callback_data='w_myself')],
        [InlineKeyboardButton('Go Back - Type of Watching', callback_data='type')]
    ]
    return InlineKeyboardMarkup(keyboard)


def action_genre_keyboard():
    res = MoviesDB.MoviesDBWrapper.movies_by_genre(['Action'])  # list of all the drama movies
    for movie in res:
        content = "Movie: " + movie.title + " | Rating: " + str(movie.rating)
        result2.append([InlineKeyboardButton(text=content,
                                             url=YouTubeConnector.YouTubeConnectorWrapper.get_trailer_url(movie))])
    result2.append([InlineKeyboardButton('Go Back - Type of Watching', callback_data='type')])
    return InlineKeyboardMarkup(result2)


def drama_genre_keyboard():
    res = MoviesDB.MoviesDBWrapper.movies_by_genre(['Drama'])  # list of all the drama movies
    for movie in res:
        content = "Movie: " + movie.title + " | Rating: "+  str(movie.rating)
        result2.append([InlineKeyboardButton(text=content,
                                             url=YouTubeConnector.YouTubeConnectorWrapper.get_trailer_url(movie))])
    result2.append([InlineKeyboardButton('Go Back - Type of Watching', callback_data='type')])
    return InlineKeyboardMarkup(result2)

####################Situation Keyboard#############################
def friends_situation_keyboard():
    res = MoviesDB.MoviesDBWrapper.movies_by_situations("Friends")
    for movie in res:
        content = "Movie: " + movie.title + " | Rating: "+  str(movie.rating)
        result.append([InlineKeyboardButton(text = content,
                                             url=YouTubeConnector.YouTubeConnectorWrapper.get_trailer_url(movie))])
    result.append([InlineKeyboardButton('Go Back - Type of Watching', callback_data='type')])
    return InlineKeyboardMarkup(result)
"""
def date_situation_keyboard():
    res = MoviesDB.MoviesDBWrapper.movies_by_situations("Date")
    for movie in res:
        content = "Movie: " + movie.title + " | Rating: "+  str(movie.rating)
        result.append([InlineKeyboardButton(text = content,
                                             url=YouTubeConnector.YouTubeConnectorWrapper.get_trailer_url(movie))])
    result.append([InlineKeyboardButton('Go Back - Type of Watching', callback_data='type')])
    return InlineKeyboardMarkup(result)"""

def family_situation_keyboard():
    res = MoviesDB.MoviesDBWrapper.movies_by_situations("Family")
    for movie in res:
        content = "Movie: " + movie.title + " | Rating: "+  str(movie.rating)
        result.append([InlineKeyboardButton(text = content,
                                             url=YouTubeConnector.YouTubeConnectorWrapper.get_trailer_url(movie))])
    result.append([InlineKeyboardButton('Go Back - Type of Watching', callback_data='type')])
    return InlineKeyboardMarkup(result)

def myself_situation_keyboard():
    res = MoviesDB.MoviesDBWrapper.movies_by_situations("Myself & I")
    for movie in res:
        content = "Movie: " + movie.title + " | Rating: "+  str(movie.rating)
        result.append([InlineKeyboardButton(text = content,
                                             url=YouTubeConnector.YouTubeConnectorWrapper.get_trailer_url(movie))])
    result.append([InlineKeyboardButton('Go Back - Type of Watching', callback_data='type')])
    return InlineKeyboardMarkup(result)

############################# Handlers #########################################
updater = Updater('1996155625:AAEck7pMRNA-HBy2h03n5ep3tkf-mRoztLk', use_context=True)

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CallbackQueryHandler(type_choose, pattern='type'))
updater.dispatcher.add_handler(CallbackQueryHandler(genre, pattern='movie_by_genre'))
updater.dispatcher.add_handler(CallbackQueryHandler(situation, pattern='movie_by_situation'))
updater.dispatcher.add_handler(CallbackQueryHandler(action_genre, pattern="action_g"))
updater.dispatcher.add_handler(CallbackQueryHandler(drama_genre, pattern="drama_g"))
updater.dispatcher.add_handler(CallbackQueryHandler(friends_situation, pattern="w_friends"))
updater.dispatcher.add_handler(CallbackQueryHandler(family_situation, pattern="w_family"))
#updater.dispatcher.add_handler(CallbackQueryHandler(date_situation, pattern="w_date"))
updater.dispatcher.add_handler(CallbackQueryHandler(myself_situation, pattern="w_myself"))
updater.start_polling()
