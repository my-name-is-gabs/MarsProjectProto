"""
This module contains a dictionary of words.
"""

dateTimeDictionary = {
    'time': ['anong oras na', 'what time is it', 'what is the time', 'oras', 'oras na', 'anong oras', 'ano oras na'],
    'date': ['anong petsa na', 'anong petsa ngayon', 'what is the date today', 'anong date ngayon', 'anong date na'],
    'today': ['anong araw na', 'anong araw ngayon', 'anong araw na ngayon', 'what day is it']
}

newsRequest = {
    'local': ['anong balita', 'anong news ngayon', 'anong balita ngayon'],
    'global': ['anong balita sa ibang bansa', 'anong world news', 'balita sa ibang bansa', 'anong update sa ibang bansa', 'anong balita abroad'],
    'showbiz': ['anong chismiz', 'anong chismis', 'anong chika', 'anong chicka']
}

weatherPrompt = ['anong lagay ng panahon ngayon', 'anong lagay ng panahon', 'lagay ng panahon']


# from gab
writingTips = {
    'prompt': ['anong tips sa pagsulat', 'any tips sa pagsusulat', 'anong tip mo sa pagsulat', 'ano ang tips mo sa pagsulat', 'tips sa pagsulat', 'anong tip sa pagsulat', 'anong writing tips mo', 'any writing tips'],
    'response': [
    'Read the sssignment, relate it to the syllabus, then, list ways it reflects the objectives of the course', 
    'Review your lecture notes to identify maini ideas that involve the writing assignment.',
    'Generate questions to answer in a paper and write key words or ideas to answer each question',
    'Answer each question to address in your paper by writing the main idea, a fruther explanation, two facts, and an example',
    'Get ready to write by allowing time to brainstorm. Use images or just begin writing notes about a word or idea.',
    'Trigger creativity by finding quotes related to important vocabulary words in your course or assignment.',
    'Work with a partner or small group to consider and flesh out ideas for papers and project.',
    'Before setting pen to page, allow 5 to 10 minutes to review your ideas, perhaps creating a diagram or chart.',
    'Only engage in brainstorming activities when you are rested and alert. Fatigue reduces rather than enhances creativity.',
    'Separate your brainstorming activities from times during which you analyze, outline, or write your ideas.',
    'Write for brief periods, perhaps 20 to 40 minutes; take a short 5 to 10 minute break, then resume writing',
    'Plan to complete a paper or presentation at least one day prior to the due date to allow for final editing',
    'Use a template or software program to write your bibliography so that all the information is formatted accurately',
    'know what you want to say before you write. Ask a question and answer it aloud before you write.',
    'Read each sentence aloud to spot spelling and grammar mistakes as well as excess wording.',
    'Check that you have sufficient facts, citations, and examples to support each major point of your paper.',
    'Always give proper credit for another\'s work by using direct quotes and citing autor, date, pupblisher and page numbers.',
    'Date and back up every revision of your paper on a thumb or external drive or email it to yourself.',
    'Pose questions and discuss the answers using a voice recorder. Write after you listen to the recording.',
    'Make a timeline and check off writing activities such as time to think, brainstorm, write, revise and edit.'
    ]
}

focusSkillTips = {
    'prompt' : ['anong tips mo para makapag focus', 'ano pang tips mo para makapagfocus', 'anong tip mo para makapag focus', 'anong tips sa pagfofocus', 'anong tip sa pag focus', 'may tip ka ba sa pagfofocus', 'my tip ka ba about sa focus', 'any tips sa focus', 'anong tips sa pag focus', 'tips to improve my focus', 'tips to improve focus', 'focus tips', 'any focus tips', 'anong focus tips mo', 'any focus tips'],
    'response': [
        'Identify places in which there are few distractions and go there to study from your most difficult courses',
        'Understand that an average person can learn and accomplish a great deal in a brief time when focused on a task.',
        'Identify times when you are mmost alert and attentive, then work on your most challenging courses',
        'Work intensely for a brief period; take a break and then review before you move on.',
        'Improve study efficiency by indetifying your best practices. When and where do you focus best when completing assignments?',
        'Keep track of the time it takes to complete diffrent types of assignments. Ask, "Am I studying when I\'m too tired or stressed?',
        'Curb ineffective hyper focus. When you work too long on a project, you dissipate your energy and accomplish little.',
        'Enhance focus and productivity by clarifying instructions and criteria for tests, papers, presentations, and projects.',
        'Stop interruptions by alerting others about the times your are unavailable because you are studying',
        'Keep a study group focused and targeted by using an agenda or questions to address. Assign someone the role of timekeeper.',
        'to curb interruptions, hang a sign obn your door such as "Genius at work. Please do not disturb."',
        'To stop distractions and interruptions, sit facing a wall, and study away from doorways and windows.',
        'Impose an Electronic Lockdown when yyou need to read or study difficult material. Turn off the phone, television, and other gadgets.',
        'If you can\'t study in total quite, use a form of white noise such as a fan or soft music.',
        'Identify places in which there are few distractions and go there to study for your most difficult courses.',
        'Stretch, get a healthy snack, or take a quick nap when you feel sluggish; a break and rest renews mental energy and focus.',
        'There is a psychological advantage to studying a particular course in the same place regularly. A routine helps trigger focus.',
        'Understand that the amount of time you can spend on each subject varies with your interest and the difficulty of the course.',
        'Set study goals to help focus your attention for specific periods-monitoring your progress helps to reinforce your efforts.',
        'Vary your study activities to avoid boredom and loss of focus. Mix the easier with more difficult problems and take breaks.',
    ]
}

# from antonio
studyTips = {
    'prompt': ['anong tips sa pag-aaral', 'anong tip sa pag-aaral', 'any tips sa pag-aaral',
               'any tips sa pag-aaral', 'anong tips mo sa pag-aaral', 'anong tip mo sa pag-aaral',
               'anong tips upang bumuti ang pag-aaral', 'anong tip upang bumuti ang pag-aaral'
               'tips to improve study', 'anong study tips mo', 'tips sa pag-aaral', 'anong study tips mo', 'any study tips'],

    'response': ['Keep yourself motivated by posting a graph on your book or computer to show number of problems your complete.',
                 'Post motivating illustrations and slogans to help you start working on your most difficult courses.',
                 'Get Plenty of sleep. Generally people need eight hours of sleep per night. Your brain needs this time to recover and organize information to strengthen its memory.',
                 'Do not do all your studying the night before. Instead spread it out, review class materials several times a week, and focus on one topic at a time',
                 'The best way to study is to focus for between forty to ninety minutes, then take a ten minute break where you do some kind of exercise. Regular exercise helps with concentration.',
                 'Working with other people can help you cover gaps in your own knowledge and also help you remember more information, since you may have to explain things to them or have conversations about the topic.',
                 'Get things done early. Start assignments as soon as they are given. Work first and have fun when you are finished.',
                 'If you prepare your own study materials then you will learn what you have studied twice: once when you make the study materials, and again when you use them to study.',
                 'Make sure to study the most difficult material when you are most alert, and do the easier ones when you are not quite as focused',
                 'Motivation is an important factor that will help you study well. This is not a complicated art or unusual technique. It is a simple as remembering to feed yourself daily.',
                 ]
}

examTips = {
    'prompt': ['anong tips sa pagsusulit', 'anong tip sa pagsusulit', 'any tips sa pagsusulit',
               'any tip sa pagsusulit', 'anong tips mo sa pagsusulit', 'anong tip mo sa pagsusulit',
               'anong tips para makapasa sa exam', 'anong tip para makapasa sa exam', 'tips to pass the exam', 'anong exam tips mo', 'any exam tips'],

    'response': ['Have someone test you on the material to find our what your weakest and strongest areas are. You can use the review questions at the end of each chapter, practice tests, or other materials',
                 'Do not forget to get enough sleep before tests. Fatigue leads to poor focus and memory',
                 'Review the results of past exams to identify your error pattern.',
                 'Separate parts of the course that require memorization of facts versus analysis of concepts or problem solving',
                 'Create flash cards for definitions, facts, and formulae. Include diagrams to facilitate memory.',
                 'Find a study buddy and create practice questions about main ideas, facts, and examples. Test each other each week.',
                 'Effective and consistent study helps you to show what you know and avoid excessive exam stress.',
                 'Create practice tests with true/false, fill in and multiple-choice questions covering each lecture or text chapter.',
                 'Clear your working space so that items do not distract you from studying.',
                 'Schedule time to reread chapter introductions, summaries, vocabulary lists and illustrations prior to exams.',
                 'Alternate study with brief exercise periods. Even running up and down stairs helps break the study stress.',
                 ]
}

# from meynard
lectureTips = {
    'prompt': ['anong tips sa pakikinig sa klase', 'anong tip sa pakikinig sa klase', 'any tips sa pakikinig sa klase',
               'any tip sa pakikinig sa klase', 'anong tip mo sa pakikinig sa klase',
               'anong tip mo sa pakikinig sa klase', 'anong tips para maintindihan ang lecture',
               'anong tip para maintindihan ang lecture', 'tips to understand the lecture', 'tips sa pakikinig sa klase', 
               'tips para sa lecture', 'anong lecture tips mo', 'any lecture tips'],

    'response': ['Preview the text before the lecture. Write or diagram a summary. Develop questions to answer during the lecture.',
                 'Review and edit your notes within twenty-four to forty-eight hours of the lecture. This enhances comprehension and memory.',
                 'Use the lecture notes as a guide to the most important aspects of the course, learning the main ideas, facts, and examples.',
                 'Use lecture notes to identify questions that you can ask in discussions or address during school hours',
                 'Audio record lectures in difficult courses; note the counter number on the bottom of the page for easy access and review.',
                 'Draw a diagram, chart, map, or timeline to summarize information presented in the lecture.',
                 'Test your retention of lecture material by visualizing graphics, reciting main ideas and then writing notes from memory.',
                 'Use your lecture to create short-answer and multiple-choice questions. Use these to locate details and prepare for tests.',
                 'Prepare your note taking paper by writing questions that you think might be addressed during the lecture.',
                 'Enlarge slides that illustrate complicated material so they are easier to read and learn in segments.',
                 'Do not assume that because you have hand outs or PowerPoint slides, you don\'t need to take lecture notes or review.',
                 'Add contextual comments or sketch doodles in your notes to emphasize facts, reflect attitudes or illustrate new terms.'
                 ]
}

readingTips = {
    'prompt': ['anong tips sa pagbabasa', 'anong tip sa pagbabasa', 'any tips sa pagbabasa',
               'any tip sa pagbabasa', 'anong tip mo sa pagbabasa', 'anong tips mo sa pagbabasa',
               'anong tips para bumuti ang aking pagbabasa', 'tips to improve my reading', 'tips sa pagbabasa', 'anong reading tips mo', 'any reading tips'],

    'response': ['View reading as a method of processing information rather than a mechanical act of reading each word.',
                 'Create diagrams and charts after you read a selection. This enhances your comprehension and retention.',
                 'Take frequent, brief breaks to relax. Read for twenty-five minutes; take a five-minute break.',
                 'Read when you are most rested and alert and least distracted. You will learn faster, greater, and enjoy better retention',
                 'Learn the elements of a diagram and then recreate it from memory on a blank page. Check accuracy and edit, if necessary',
                 'Create short quizzes to test your understanding of the material you have read for each assignment.',
                 'Summarize out loud the main ideas that you learn. Schedule three to five minutes for every thirty minutes you study',
                 'Create a mental image about hte information you are reading. Remember that one picture is worth a thousand words.',
                 'View vocabulary as a basic building block of comprehension and use illustrations to help understand and memorize meaning.',
                 'Take time to relax before you read; stretch and take a few deep breaths, then energize by visualizing a past success.']
}

if __name__ == '__main__':
    print(len(writingTips['response']))
