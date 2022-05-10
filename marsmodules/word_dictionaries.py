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
    'prompt' : ['anong tips mo para makapag focus', 'ano pang tips mo para makapagfocus', 'anong tip mo para makapag focus', 'anong tips sa pagfofocus', 'anong tip sa pag focus', 'may tip ka ba sa pagfofocus', 'my tip ka ba about sa focus', 'any tips sa focus', 'anong tips sa pag focus', 'tips to improve my focus', 'tips to improve focus'],
    'response': [
        'Remember, the better your focus, the better your ability to learn an retain information.',
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

if __name__ == '__main__':
    print(len(writingTips['response']))
