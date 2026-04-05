import re
import os

content = """
28.03.2023

<a href="https://www.goodreads.com/book/show/20911932-warhammer-40-000" style="float: left; padding-right: 20px"><img border="0" alt="Warhammer 40,000: Sisters of Battle" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1645102108l/20911932._SX98_.jpg" /></a><a href="https://www.goodreads.com/book/show/20911932-warhammer-40-000">Warhammer 40,000: Sisters of Battle</a> by <a href="https://www.goodreads.com/author/show/19241779.Torunn_Gr_nbekk">Torunn Grønbekk</a><br/>
My rating: <a href="https://www.goodreads.com/review/show/5446727888">3 of 5 stars</a><br /><br />
It does show a little bit of the warhammer universe - how it looks outside of the books, and since it is a comic and has probably less than a 100 pages I'd say it is worth the read. <br />It has beautiful illustrations, but overall it's a bit crowded. There were too many people in the one big team, so I never remembered any of the sister's names. <br />The book also has some cool and useful information about the sisters and the heretics, so this was a great read from the point of someone new to the warhammer universe.
<br/><br/>
<a href="https://www.goodreads.com/review/list/163394279-david-stra-k">View all my reviews</a>


26.03.2023

<a href="https://www.goodreads.com/book/show/1858150.Witch_Hunter" style="float: left; padding-right: 20px"><img border="0" alt="Witch Hunter" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1189299275l/1858150._SX98_.jpg" /></a><a href="https://www.goodreads.com/book/show/1858150.Witch_Hunter">Witch Hunter</a> by <a href="https://www.goodreads.com/author/show/22087105.C_L_Werner">C.L.   Werner</a><br/>
My rating: <a href="https://www.goodreads.com/review/show/5389246133">4 of 5 stars</a><br /><br />
A good book with nice worldbuilding that unfortunately did not really deliver near the end. There wasn't really a payoff - the book did not have a point and nothing much was solved.<br />The character of the witch hunter is an awesome one though and it was fun reading about him, though I would be more positive if the book was not just a setup for an another book.
<br/><br/>
<a href="https://www.goodreads.com/review/list/163394279-david-stra-k">View all my reviews</a>


20.03.2023

<a href="https://www.goodreads.com/book/show/1052311.Ravenor" style="float: left; padding-right: 20px"><img border="0" alt="Ravenor (Ravenor #1)" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1387712799l/1052311._SY160_.jpg" /></a><a href="https://www.goodreads.com/book/show/1052311.Ravenor">Ravenor</a> by <a href="https://www.goodreads.com/author/show/33262.Dan_Abnett">Dan Abnett</a><br/>
My rating: <a href="https://www.goodreads.com/review/show/5388827559">5 of 5 stars</a><br /><br />
Although sometimes I was lost on the story, the book is an awesome introduction into the warhammer universe. There were some Eisenhorn references, but not a lot, characters are interesting, ravenor is badass, I want to see more of them :D.
<br/><br/>
<a href="https://www.goodreads.com/review/list/163394279-david-stra-k">View all my reviews</a>


08.03.2023

<a href="https://www.goodreads.com/book/show/523699.Headhunters" style="float: left; padding-right: 20px"><img border="0" alt="Headhunters (Shadowrun, #27)" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1175529422l/523699._SY160_.jpg" /></a><a href="https://www.goodreads.com/book/show/523699.Headhunters">Headhunters</a> by <a href="https://www.goodreads.com/author/show/12275.Mel_Odom">Mel Odom</a><br/>
My rating: <a href="https://www.goodreads.com/review/show/5388835956">4 of 5 stars</a><br /><br />
This book featured one of my most favourite shadowrunning squads with everyone having enough personality and possibilities to do cool things. <br />The characters were relatable and seemed real, although outside of the team I feel like all people were really generic, without some kind of a shtick or something to show their personality or motivation. <br />The book didn't leave much loose ends and most setu-ps were paid-off :D. Though at some points in the book some established characters don't show up without an explanation to the reason, which makes me feel like they should've been there and should've changed the outcome.
<br/><br/>
<a href="https://www.goodreads.com/review/list/163394279-david-stra-k">View all my reviews</a>


04.03.2023

<a href="https://www.goodreads.com/book/show/830502.It" style="float: left; padding-right: 20px"><img border="0" alt="It" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1334416842l/830502._SY160_.jpg" /></a><a href="https://www.goodreads.com/book/show/830502.It">It</a> by <a href="https://www.goodreads.com/author/show/3389.Stephen_King">Stephen  King</a><br/>
My rating: <a href="https://www.goodreads.com/review/show/5390227080">5 of 5 stars</a><br /><br />
A classic and genre defining coming of age story by one of the best written authors ever.
<br/><br/>
<a href="https://www.goodreads.com/review/list/163394279-david-stra-k">View all my reviews</a>


04.03.2023

<a href="https://www.goodreads.com/book/show/351450.Choose_Your_Enemies_Carefully" style="float: left; padding-right: 20px"><img border="0" alt="Choose Your Enemies Carefully (Shadowrun: Secrets of Power, #2)" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1388724366l/351450._SY160_.jpg" /></a><a href="https://www.goodreads.com/book/show/351450.Choose_Your_Enemies_Carefully">Choose Your Enemies Carefully</a> by <a href="https://www.goodreads.com/author/show/201555.Robert_N_Charrette">Robert N. Charrette</a><br/>
My rating: <a href="https://www.goodreads.com/review/show/5389261520">5 of 5 stars</a><br /><br />
A great addition in the secrets of power series that I did not regret reading. It continues the first book "Never deal with a dragon" and it does a fantastic job, succeeding at the same things as the first book. The story is interesting, this time exploring the elven parts of America and the characters are awesome as always.
<br/><br/>
<a href="https://www.goodreads.com/review/list/163394279-david-stra-k">View all my reviews</a>


04.03.2023

<a href="https://www.goodreads.com/book/show/351451.Never_Deal_with_a_Dragon" style="float: left; padding-right: 20px"><img border="0" alt="Never Deal with a Dragon (Shadowrun: Secrets of Power, #1)" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1388724363l/351451._SY160_.jpg" /></a><a href="https://www.goodreads.com/book/show/351451.Never_Deal_with_a_Dragon">Never Deal with a Dragon</a> by <a href="https://www.goodreads.com/author/show/201555.Robert_N_Charrette">Robert N. Charrette</a><br/>
My rating: <a href="https://www.goodreads.com/review/show/5389260433">5 of 5 stars</a><br /><br />
The best introduction to shadowrunning literature that I could wish for. This story sets up interesting characters, really cool story and makes a lot of cool things happen during it. <br />It is the origins story of a legend.
<br/><br/>
<a href="https://www.goodreads.com/review/list/163394279-david-stra-k">View all my reviews</a>


04.03.2023

<a href="https://www.goodreads.com/book/show/351455.Find_Your_Own_Truth" style="float: left; padding-right: 20px"><img border="0" alt="Find Your Own Truth (Shadowrun: Secrets of Power, #3)" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1387708407l/351455._SY160_.jpg" /></a><a href="https://www.goodreads.com/book/show/351455.Find_Your_Own_Truth">Find Your Own Truth</a> by <a href="https://www.goodreads.com/author/show/201555.Robert_N_Charrette">Robert N. Charrette</a><br/>
My rating: <a href="https://www.goodreads.com/review/show/5389261573">5 of 5 stars</a><br /><br />
This book is the big boom at the end of the Secrets of Power trilogy. The ending is 100% deserved and it solves everything that was set-up, which is impressive. This book also fleshes out Dodger, who is a lovable character with his personality and way of speaking.<br />What a way to go. I enjoyed this very much.
<br/><br/>
<a href="https://www.goodreads.com/review/list/163394279-david-stra-k">View all my reviews</a>


04.03.2023

<a href="https://www.goodreads.com/book/show/351457.Just_Compensation" style="float: left; padding-right: 20px"><img border="0" alt="Just Compensation" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1173993241l/351457._SY160_.jpg" /></a><a href="https://www.goodreads.com/book/show/351457.Just_Compensation">Just Compensation</a> by <a href="https://www.goodreads.com/author/show/201555.Robert_N_Charrette">Robert N. Charrette</a><br/>
My rating: <a href="https://www.goodreads.com/review/show/5388830179">2 of 5 stars</a><br /><br />
At first it was a cool experience, with some favourable side characters like dodger appearing. Then it got really convoluted though. <br /><br />The team of shadowrunners is pretty lovable with interesting characters. <br />I feel like so many things were set up but only about a third or a quarter of them actually had any kind of payoff. <br />The story was all over the place and I had no idea what was happening for about 30% of the book. Everything was chaotic. <br /><br />Overall a meh read, but atleast I got to know the general map of the American shadowrunning universe - including a map of America in that time.
<br/><br/>
<a href="https://www.goodreads.com/review/list/163394279-david-stra-k">View all my reviews</a>

04.03.2023

<a href="https://www.goodreads.com/book/show/40651883-snow-crash" style="float: left; padding-right: 20px"><img border="0" alt="Snow Crash" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1589842551l/40651883._SX98_.jpg" /></a><a href="https://www.goodreads.com/book/show/40651883-snow-crash">Snow Crash</a> by <a href="https://www.goodreads.com/author/show/545.Neal_Stephenson">Neal Stephenson</a><br/>
My rating: <a href="https://www.goodreads.com/review/show/5389849339">4 of 5 stars</a><br /><br />
A very strong book that is all at once funny, while you have to think about the plot. Everything that was happening here and there was reading great. <br />One segment that was not reading as well was a segment that went back into the past. I felt as if the book was trying to be way too deep for it. <br />After that was over though, the book went back to being hilarious and interesting with a great final battle!
<br/><br/>
<a href="https://www.goodreads.com/review/list/163394279-david-stra-k">View all my reviews</a>


04.03.2023

<a href="https://www.goodreads.com/book/show/1131232.Shadowrun_14" style="float: left; padding-right: 20px"><img border="0" alt="Shadowrun 14: Nosferatu" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1181243367l/1131232._SY160_.jpg" /></a><a href="https://www.goodreads.com/book/show/1131232.Shadowrun_14">Shadowrun 14: Nosferatu</a> by <a href="https://www.goodreads.com/author/show/305518.Carl_Sargent">Carl Sargent</a><br/>
My rating: <a href="https://www.goodreads.com/review/show/5388853327">3 of 5 stars</a><br /><br />
Well, first things first, when you look at the cover of the book you see a vampire dashing through the streets of a town. That is not what this book is about. <br />This book is more about a guy who meets a few other people and travels the world with them, with some tension and aggression here and there, but ultimately without much action happening. That is except the big final battle with the main bad guy, who I guess, no one else could stop, except our main hero who this book is about. <br />Now, the book is pretty fun and interesting, but ultimately kinda not as expected. There are much cooler things to do with vampires, but here they were just a generic thing to smash in the end without much of a personality.<br />The book is finished though, things make sense and the setups are paid off.
<br/><br/>
<a href="https://www.goodreads.com/review/list/163394279-david-stra-k">View all my reviews</a>


25.10.2024

<a href="https://www.goodreads.com/book/show/1261049.House_of_Hell" style="float: left; padding-right: 20px"><img border="0" alt="House of Hell (Fighting Fantasy #10)" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1457004279l/1261049._SY160_.jpg" /></a><a href="https://www.goodreads.com/book/show/1261049.House_of_Hell">House of Hell</a> by <a href="https://www.goodreads.com/author/show/2925619.Steve_Jackson">Steve   Jackson</a><br/>
My rating: <a href="https://www.goodreads.com/review/show/6424614812">2 of 5 stars</a><br /><br />
If you want a story-led game book where you make important decisions and everything you do matters, then look elsewhere, because this gamebook is totally luck based.<br /><br />It's the fighting fantasy classic, where you wander randomly into rooms that have no indication about what's in them, so you're just randomly going into rooms. Oh, but don't go into some specific rooms, because you will lose half your sanity and you'll have to restart.<br /><br />For me this gamebook was fun at first, but after I saw what's inside the rooms, the gamebook got tedious. I was so confused about what to do that I decided to check out a guide to be able to finish this thing.<br /><br />I would suggest finding a different game book, or maybe just keep away from Fighting Fantasy gamebooks as all of them are like this.
<br/><br/>
<a href="https://www.goodreads.com/review/list/163394279-david-stra-k">View all my reviews</a>
"""

entries = re.split(r'(?=\n\d{2}\.\d{2}\.\d{4}\n)', '\n' + content)
blocks = [b.strip() for b in entries if b.strip()]

for block in blocks:
    lines = block.split('\n', 1)
    date_str = lines[0].strip()
    html_content = lines[1].strip() if len(lines) > 1 else ""
    
    title_match = re.search(r'<a href="[^"]*">([^<]+)</a> by', html_content)
    if not title_match: continue
    title = title_match.group(1)
    
    author_match = re.search(r'by <a href="[^"]*">([^<]+)</a>', html_content)
    author = author_match.group(1) if author_match else ""
    author = " ".join(author.split())
    
    rating_match = re.search(r'(\d+) of 5 stars', html_content)
    rating = int(rating_match.group(1)) if rating_match else 0
    
    img_match = re.search(r'src="([^"]+)"', html_content)
    if not img_match: continue
    img_url = img_match.group(1)
    
    img_url = re.sub(r'_[SXY]\w+_', '_SY475_', img_url)
    html_content = re.sub(r'_[SXY]\w+_', '_SY475_', html_content)
    
    day, month, year = date_str.split('.')
    iso_date = f"{year}-{month}-{day}T12:00:00+00:00"
    
    filename = title.lower()
    filename = re.sub(r'[^a-z0-9\s-]', '', filename)
    filename = re.sub(r'[\s-]+', '_', filename) + '.md'
    
    tags = '["book", "review"]'
    if "warhammer" in filename or "ravenor" in filename or "sisters_of_battle" in filename or re.search(r'(witch\shunter)', title, re.I):
        tags = '["book", "review", "warhammer 40k", "sci-fi"]'
    if "shadowrun" in filename or "never_deal" in filename or "enemy" in filename or "truth" in filename or "compensation" in filename or "headhunters" in filename:
        tags = '["book", "review", "shadowrun", "cyberpunk", "sci-fi"]'
    if "snow_crash" in filename:
        tags = '["book", "review", "cyberpunk", "sci-fi"]'
    if "it" == filename.replace(".md", "") or "house_of_hell" in filename:
        tags = '["book", "review", "horror"]'
        
    md_content = f"""+++
date = '{iso_date}'
title = '{title}'
author = '{author}'
rating = {rating}
cover_image = '{img_url}'
tags = {tags}
+++
{html_content}
"""
    
    filepath = os.path.join('content/book', filename)
    with open(filepath, 'w', encoding='utf-8') as out:
        out.write(md_content)
    print(f"Created {filepath}")

