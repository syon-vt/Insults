from pyautogui import write, press
from time import sleep

insult = "Don't care + didn't ask + L + Ratio + soyjak + beta + cringe + stfu + cope + seethe + ok boomer + incel + virgin + Karen + clownclownclown + you are not just a clown, you are the entire circus + nail_carenail_carenail_care + nah this ain't it + do better + check your privilege + pronouns in bio + anime pfp + nauseated_facenauseated_faceface_vomitingface_vomiting + the cognitive dissonance is real with this one + small dick energy + joyjoyroflrofl + lol copium + snowflake + triangular_flag_on_posttriangular_flag_on_posttriangular_flag_on_post + those tears taste delicious + Lisa Simpson meme template saying that your opinion is wrong + unamusedrolling_eyesface_with_monocleface_with_raised_eyebrow + wojak meme in which I'm the chad + average your opinion fan vs average my opinion enjoyer + random k-pop fan + cry more + how's your wife's boyfriend doing + Cheetos breath + Intelligence 0 + r/whooooosh + r/downvotedtooblivion + blocked and reported + yo Momma so fat + I fucked your mom last night + what zero pussy does to a mf + Jesse what the fuck are you talking about + holy shit go touch some grass + cry about it + get triggered + you fell off"
clean_insult = "Don't care + didn't ask + L + Ratio + beta + cringe + shut up + cope + ok boomer + Karen + clownclownclown + you are not just a clown, you are the entire circus + nah this ain't it + do better + check your privilege + pronouns in bio + anime pfp + nauseated_facenauseated_faceface_vomitingface_vomiting + the cognitive dissonance is real with this one + joyjoyroflrofl + lol copium + snowflake + triangular_flag_on_posttriangular_flag_on_posttriangular_flag_on_post + those tears taste delicious + Lisa Simpson meme template saying that your opinion is wrong + unamusedrolling_eyesface_with_monocleface_with_raised_eyebrow + average your opinion fan vs average my opinion enjoyer + random k-pop fan + cry more + Cheetos breath + Intelligence 0 + r/whooooosh + r/downvotedtooblivion + blocked and reported + Jesse what the hell are you talking about + go touch some grass + cry about it + get triggered + you fell off"

def timer(sec, text):
    while sec >= 0:
        print(f"{text}: {sec}", end='\r')
        sec -= 1
        sleep(1)
    print()

def main(version):
    timer(5, "Starting in")
    dict = version.split(" + ")

    for word in dict:
        write(word)
        sleep(0.25)
        press('enter')
        sleep(0.25)


yn = input("Clean Version y/n? ")

if yn == "y":
    main(clean_insult)
elif yn == "n":
    main(insult)