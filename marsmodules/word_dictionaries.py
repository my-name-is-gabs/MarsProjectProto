"""
This module contains a dictionary of words.
"""

dateTimeDictionary = {
    'time': ['anong oras na', 'what time is it', 'what is the time', 'oras'],
    'date': ['anong petsa na', 'anong petsa ngayon', 'what is the date today', 'anong date ngayon', 'anong date na'],
    'today': ['anong araw na', 'anong araw ngayon', 'anong araw na ngayon', 'what day is it']
}

newsRequest = {
    'local': ['anong balita', 'anong news ngayon', 'anong balita ngayon'],
    'global': ['anong balita sa ibang bansa', 'anong world news', 'balita sa ibang bansa', 'anong update sa ibang bansa', 'anong balita abroad'],
    'showbiz': ['anong chismiz', 'anong chismis', 'anong latest']
}

weatherPrompt = ['anong lagay ng panahon ngayon', 'anong lagay ng panahon', 'lagay ng panahon']

closeAppDictionary = ['bye-bye mars', 'paalam mars', 'exit', 'goodbye mars', 'bye-bye', 'bye mars', 'close mars', 'exit mars']

# from gab
writingTips = {
    'prompt': ['anong tips sa pagsulat', 'any tips sa pagsusulat', 'anong tip mo sa pagsulat', 'ano ang tips mo sa pagsulat', 'tips sa pagsulat', 'anong tip sa pagsulat'],
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
    'Separate your brainstorming activities from times during which you analyze, outline, or write your ideas.'
    ]
}

focusSkillTips = {
    'prompt' : ['anong tips mo para makapag focus', 'ano pang tips mo para makapagfocus', 'anong tip mo para makapag focus', 'anong tips sa pagfofocus', 'anong tip sa pag focus', 'may tip ka ba sa pagfofocus', 'my tip ka ba about sa focus', 'any tips sa focus', 'anong tips sa pag focus', 'tips to improve my focus', 'tips to improve focus', 'focus tips'],
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
        'Keep a study group focused and targeted by using an agenda or questions to address. Assign someone the role of timekeeper.'
    ]
}

# from antonio
studyTips = {
    'prompt': ['anong tips sa pag-aaral', 'anong tip sa pag-aaral', 'any tips sa pag-aaral',
               'any tips sa pag-aaral', 'anong tips mo sa pag-aaral', 'anong tip mo sa pag-aaral',
               'anong tips upang bumuti ang pag-aaral', 'anong tip upang bumuti ang pag-aaral'
               'tips to improve study'],

    'response': ['Keep yourself motivated by posting a graph on your book or computer to show number of problems your complete.',
                 'Post motivating illustrations and slogans to help you start working on your most difficult courses.',
                 'Get Plenty of sleep. Generally people need eight hours of sleep per night. Your brain needs this time to recover and organize information to strengthen its memory.',
                 'Do not do all your studying the night before. Instead spread it out, review class materials several times a week, and focus on one topic at a time',
                 'The best way to study is to focus for between forty to ninety minutes, then take a ten minute break where you do some kind of exercise. Regular exercise helps with concentration.',
                 'Working with other people can help you cover gaps in your own knowledge and also help you remember more information, since you may have to explain things to them or have conversations about the topic.',
                 'Get things done early. Start assignments as soon as they are given. Work first and have fun when you are finished.',
                 'If you prepare your own study materials then you will learn what you have studied twice: once when you make the study materials, and again when you use them to study.',
                 'Make sure to study the most difficult material when you are most alert, and do the easier ones when you are not quite as focused',
                 'Motivation is an important factor that will help you study well. This is not a complicated art or unusual technique. It is a simple as remembering to feed yourself daily.']
}

examTips = {
    'prompt': ['anong tips sa pagsusulit', 'anong tip sa pagsusulit', 'any tips sa pagsusulit',
               'any tip sa pagsusulit', 'anong tips mo sa pagsusulit', 'anong tip mo sa pagsusulit',
               'anong tips para makapasa sa exam', 'anong tip para makapasa sa exam', 'tips to pass the exam'],

    'response': ['Have someone test you on the material to find our what your weakest and strongest areas are. You can use the review questions at the end of each chapter, practice tests, or other materials',
                 'Do not forget to get enough sleep before tests. Fatigue leads to poor focus and memory',
                 'Review the results of past exams to identify your error pattern.',
                 'Separate parts of the course that require memorization of facts versus analysis of concepts or problem solving',
                 'Create flash cards for definitions, facts, and formulae. Include diagrams to facilitate memory.',
                 'Find a study buddy and create practice questions about main ideas, facts, and examples. Test each other each week.',
                 'Effective and consistent study helps you to show what you know and avoid excessive exam stress.',
                 'Create practice tests with true/false, fill in and multiple-choice questions covering each lecture or text chapter.',
                 'Clear your working space so that items do not distract you from studying.',
                 'Schedule time to reread chapter introductions, summaries, vocabulary lists and illustrations prior to exams.']
}

# from meynard
lectureTips = {
    'prompt': ['anong tips sa pakikinig sa klase', 'anong tip sa pakikinig sa klase', 'any tips sa pakikinig sa klase',
               'any tip sa pakikinig sa klase', 'anong tip mo sa pakikinig sa klase',
               'anong tip mo sa pakikinig sa klase', 'anong tips para maintindihan ang lecture',
               'anong tip para maintindihan ang lecture', 'tips to understand the lecture', 'tips sa pakikinig sa klase'],

    'response': ['Preview the text before the lecture. Write or diagram a summary. Develop questions to answer during the lecture.',
                 'Review and edit your notes within twenty-four to forty-eight hours of the lecture. This enhances comprehension and memory.',
                 'Use the lecture notes as a guide to the most important aspects of the course, learning the main ideas, facts, and examples.',
                 'Use lecture notes to identify questions that you can ask in discussions or address during school hours',
                 'Audio record lectures in difficult courses; note the counter number on the bottom of the page for easy access and review.',
                 'Draw a diagram, chart, map, or timeline to summarize information presented in the lecture.',
                 'Test your retention of lecture material by visualizing graphics, reciting main ideas and then writing notes from memory.',
                 'Use your lecture to create short-answer and multiple-choice questions. Use these to locate details and prepare for tests.',
                 'Prepare your note taking paper by writing questions that you think might be addressed during the lecture.',
                 'Enlarge slides that illustrate complicated material so they are easier to read and learn in segments.']
}

readingTips = {
    'prompt': ['anong tips sa pagbabasa', 'anong tip sa pagbabasa', 'any tips sa pagbabasa',
               'any tip sa pagbabasa', 'anong tip mo sa pagbabasa', 'anong tips mo sa pagbabasa',
               'anong tips para bumuti ang aking pagbabasa', 'tips to improve my reading'],

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
