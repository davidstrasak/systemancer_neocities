import re
import os

books = [
    {
        "date": "2023-11-28T12:00:00+00:00",
        "title": "William King - Trollslayer",
        "file": "content/book/trollslayer.md",
        "tags": '["Fantasy", "Warhammer Fantasy", "Short Stories"]',
        "html": """<a href="https://www.goodreads.com/book/show/691915.Trollslayer" style="float: left; padding-right: 20px"><img border="0" alt="Trollslayer (Gotrek & Felix, #1)" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1177284384l/691915._SY475_.jpg" /></a><a href="https://www.goodreads.com/book/show/691915.Trollslayer">Trollslayer</a> by <a href="https://www.goodreads.com/author/show/48348.William_King">William  King</a><br/>
My rating: <a href="https://www.goodreads.com/review/show/5962195173">4 of 5 stars</a><br /><br />
An interesting read, because it is more like a collection of short stories with an ongoing narrative, rather than a normal novel. You mostly see the things happen from our heroes' point of view, but it's cool.<br />Definitely an inspiration for a bunch of my next dnd stories. I love the character of gotrek. I will read more books in this saga :D.
<br/><br/>
<a href="https://www.goodreads.com/review/list/163394279-david-stra-k">View all my reviews</a>"""
    },
    {
        "date": "2023-11-28T12:00:00+00:00",
        "title": "Mike Brooks - Harrowmaster",
        "file": "content/book/harrowmaster.md",
        "tags": '["Sci-Fi", "Warhammer 40k", "Fiction"]',
        "html": """<a href="https://www.goodreads.com/book/show/63123245-harrowmaster" style="float: left; padding-right: 20px"><img border="0" alt="Harrowmaster (Renegades)" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1667023024l/63123245._SY475_.jpg" /></a><a href="https://www.goodreads.com/book/show/63123245-harrowmaster">Harrowmaster</a> by <a href="https://www.goodreads.com/author/show/204204.Mike_Brooks">Mike Brooks</a><br/>
My rating: <a href="https://www.goodreads.com/review/show/5914397997">5 of 5 stars</a><br /><br />
My first alpha legion story and I hope it's not the last one. They really feel like they have a plan for everything and they feel really unique, since it's a traitor legion, but does not feel traitorous.
<br/><br/>
<a href="https://www.goodreads.com/review/list/163394279-david-stra-k">View all my reviews</a>"""
    },
    {
        "date": "2023-08-17T12:00:00+00:00",
        "title": "Paul Tobin - The Witcher, Vol. 1: House of Glass",
        "file": "content/book/the_witcher_vol_1_house_of_glass.md",
        "tags": '["Comic", "Fantasy", "The Witcher"]',
        "html": """<a href="https://www.goodreads.com/book/show/21544276-the-witcher-vol-1" style="float: left; padding-right: 20px"><img border="0" alt="The Witcher, Vol. 1: House of Glass" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1554458247l/21544276._SY475_.jpg" /></a><a href="https://www.goodreads.com/book/show/21544276-the-witcher-vol-1">The Witcher, Vol. 1: House of Glass</a> by <a href="https://www.goodreads.com/author/show/440975.Paul_Tobin">Paul Tobin</a><br/>
<br /><br />

<br/><br/>
<a href="https://www.goodreads.com/review/list/163394279-david-stra-k">View all my reviews</a>"""
    },
    {
        "date": "2023-10-17T12:00:00+00:00",
        "title": "Rafał Jaki - The Witcher: Ronin",
        "file": "content/book/the_witcher_ronin.md",
        "tags": '["Comic", "Manga", "The Witcher"]',
        "html": """<a href="https://www.goodreads.com/book/show/60568782-the-witcher" style="float: left; padding-right: 20px"><img border="0" alt="The Witcher: Ronin" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1646681004l/60568782._SY475_.jpg" /></a><a href="https://www.goodreads.com/book/show/60568782-the-witcher">The Witcher: Ronin</a> by <a href="https://www.goodreads.com/author/show/22284240.Rafa_Jaki">Rafał Jaki</a><br/>
<br /><br />

<br/><br/>
<a href="https://www.goodreads.com/review/list/163394279-david-stra-k">View all my reviews</a>"""
    },
    {
        "date": "2023-09-13T12:00:00+00:00",
        "title": "Robert T. Kiyosaki - Rich Dad Poor Dad: What the Rich Teach Their Kids about Money",
        "file": "content/book/rich_dad_poor_dad.md",
        "tags": '["Finance", "Self-Help", "Non-Fiction"]',
        "html": """<a href="https://www.goodreads.com/book/show/52037104-rich-dad-poor-dad" style="float: left; padding-right: 20px"><img border="0" alt="Rich Dad Poor Dad: What the Rich Teach Their Kids about Money" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1569289490l/52037104._SY475_.jpg" /></a><a href="https://www.goodreads.com/book/show/52037104-rich-dad-poor-dad">Rich Dad Poor Dad: What the Rich Teach Their Kids about Money</a> by <a href="https://www.goodreads.com/author/show/600.Robert_T_Kiyosaki">Robert T. Kiyosaki</a><br/>
My rating: <a href="https://www.goodreads.com/review/show/5730968397">5 of 5 stars</a><br /><br />
What a masterpiece. I bought this book as my first self help "improvement" book because I read it inside a bookstore and I'm really glad I did.<br /><br />Before I bought this book I thought that improvement literature would be boring, but this book proved me wrong. <br /><br />It is a really interesting topic, tons of good points, and the readibility of the book is splendid. It reads like a story driven fantasy fiction, but it is real and it teaches you.<br /><br />In addition to that there are new study sessions and recaps after every chapter, so I will definetly revisit the book and read the summaries in a year (or rather every year from now on :D).<br /><br />As for negatives, there are some advertisements to Robert's game Cashflow, but I actually expected that, since he is a sales person. Nontheless they were there with a point to learn or show something, so the only negative is hardly a negative.<br /><br />Best self help book I've read.
<br/><br/>
<a href="https://www.goodreads.com/review/list/163394279-david-stra-k">View all my reviews</a>"""
    },
    {
        "date": "2023-09-09T12:00:00+00:00",
        "title": "Alan Moore - Watchmen: The Deluxe Edition",
        "file": "content/book/watchmen_the_deluxe_edition.md",
        "tags": '["Comic", "Graphic Novel", "Fiction"]',
        "html": """<a href="https://www.goodreads.com/book/show/73579070-watchmen" style="float: left; padding-right: 20px"><img border="0" alt="Watchmen: The Deluxe Edition" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1677898514l/73579070._SY475_.jpg" /></a><a href="https://www.goodreads.com/book/show/73579070-watchmen">Watchmen: The Deluxe Edition</a> by <a href="https://www.goodreads.com/author/show/3961.Alan_Moore">Alan             Moore</a><br/>
My rating: <a href="https://www.goodreads.com/review/show/5730974644">5 of 5 stars</a><br /><br />
The book was a little stale in the middle, but when you read the ending, everything shown before started to make sense.<br />I love how all the characters are flawed - that really makes it more realistic and that's why this book is a masterpiece.
<br/><br/>
<a href="https://www.goodreads.com/review/list/163394279-david-stra-k">View all my reviews</a>"""
    },
    {
        "date": "2023-09-02T12:00:00+00:00",
        "title": "John French - Ahriman: Unchanged",
        "file": "content/book/ahriman_unchanged.md",
        "tags": '["Sci-Fi", "Warhammer 40k", "Fiction"]',
        "html": """<a href="https://www.goodreads.com/book/show/25111351-ahriman" style="float: left; padding-right: 20px"><img border="0" alt="Ahriman: Unchanged (Ahriman #3)" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1435413388l/25111351._SY475_.jpg" /></a><a href="https://www.goodreads.com/book/show/25111351-ahriman">Ahriman: Unchanged</a> by <a href="https://www.goodreads.com/author/show/6525693.John_French">John  French</a><br/>
My rating: <a href="https://www.goodreads.com/review/show/5703799396">4 of 5 stars</a><br /><br />
Ahriman stories are overall really complicated, but epic, and this is no exception. It was pretty hard to read, but I'm glad I did it.<br />On the complicated part I had to look up some stuff of the warhammer lore wiki, and sometimes I did not know what was happening exactly, but the epic fights and the overall story saved it and made it worth it.
<br/><br/>
<a href="https://www.goodreads.com/review/list/163394279-david-stra-k">View all my reviews</a>"""
    },
    {
        "date": "2023-09-02T12:00:00+00:00",
        "title": "John French - Ahriman: The Omnibus",
        "file": "content/book/ahriman_the_omnibus.md",
        "tags": '["Sci-Fi", "Warhammer 40k", "Fiction"]',
        "html": """<a href="https://www.goodreads.com/book/show/30753526-ahriman" style="float: left; padding-right: 20px"><img border="0" alt="Ahriman: The Omnibus (Ahriman #1-3)" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1490524489l/30753526._SY475_.jpg" /></a><a href="https://www.goodreads.com/book/show/30753526-ahriman">Ahriman: The Omnibus</a> by <a href="https://www.goodreads.com/author/show/6525693.John_French">John  French</a><br/>
My rating: <a href="https://www.goodreads.com/review/show/5813753403">3 of 5 stars</a><br /><br />
This omnibus is a good starting point if you want to read about the thousand sons or space marines overall for the first time. <br />I was a great and an epic read, but I kinda regret that Ahriman does not appear that much in later pages so we don't really see him as a character - even though it's his story. It also felt a little bit futile, since the outcome of a bunch of stories is given in advance (for example you see a story is told by a character, so I know he survives).<br />Finally I felt like the stories all weave into each other and in the end there is so much stuff to cover and think about and a few of these stories feel futile. Other than that though the story was interesting and exciting. Lots of big stuff happening, lots of epic moments, and pretty interesting characters - at least those who were introduced.<br />All in all it was a decent read. This book did not cost me much and it really is a bang for your buck - It's 1,5x the price of a normal book, but it contains 3 books and really interesting short stories. It's a great and affordable start with space marine stories.
<br/><br/>
<a href="https://www.goodreads.com/review/list/163394279-david-stra-k">View all my reviews</a>"""
    },
    {
        "date": "2023-07-25T12:00:00+00:00",
        "title": "Gary Kloster - The Perfect Assassin",
        "file": "content/book/the_perfect_assassin.md",
        "tags": '["Sci-Fi", "Warhammer 40k", "Short Stories"]',
        "html": """<a href="https://www.goodreads.com/book/show/57194514-the-perfect-assassin" style="float: left; padding-right: 20px"><img border="0" alt="The Perfect Assassin (Black Library Celebration 2021 #3)" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1614164233l/57194514._SY475_.jpg" /></a><a href="https://www.goodreads.com/book/show/57194514-the-perfect-assassin">The Perfect Assassin</a> by <a href="https://www.goodreads.com/author/show/6479891.Gary_Kloster">Gary Kloster</a><br/>
My rating: <a href="https://www.goodreads.com/review/show/5718440288">5 of 5 stars</a><br /><br />
An awesome, funny, but still interesting short story! My favourite of the 3 short stories I've read so far. Now I'm thrilled for more short stories from the anthology book I'm reading.
<br/><br/>
<a href="https://www.goodreads.com/review/list/163394279-david-stra-k">View all my reviews</a>"""
    },
    {
        "date": "2023-07-18T12:00:00+00:00",
        "title": "John French - Ahriman: Hand of Dust",
        "file": "content/book/ahriman_hand_of_dust.md",
        "tags": '["Sci-Fi", "Warhammer 40k", "Short Stories"]',
        "html": """<a href="https://www.goodreads.com/book/show/19097331-ahriman" style="float: left; padding-right: 20px"><img border="0" alt="Ahriman: Hand of Dust (Black Library Advent Calendar 2013 #2)" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1385985628l/19097331._SY475_.jpg" /></a><a href="https://www.goodreads.com/book/show/19097331-ahriman">Ahriman: Hand of Dust</a> by <a href="https://www.goodreads.com/author/show/6525693.John_French">John  French</a><br/>
<br /><br />

<br/><br/>
<a href="https://www.goodreads.com/review/list/163394279-david-stra-k">View all my reviews</a>"""
    },
    {
        "date": "2023-07-22T12:00:00+00:00",
        "title": "John French - King of Ashes",
        "file": "content/book/king_of_ashes.md",
        "tags": '["Sci-Fi", "Warhammer 40k", "Short Stories"]',
        "html": """<a href="https://www.goodreads.com/book/show/33972900-king-of-ashes" style="float: left; padding-right: 20px"><img border="0" alt="King of Ashes (Ahriman)" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1485189593l/33972900._SY475_.jpg" /></a><a href="https://www.goodreads.com/book/show/33972900-king-of-ashes">King of Ashes</a> by <a href="https://www.goodreads.com/author/show/6525693.John_French">John  French</a><br/>
My rating: <a href="https://www.goodreads.com/review/show/5703799003">5 of 5 stars</a><br /><br />

<br/><br/>
<a href="https://www.goodreads.com/review/list/163394279-david-stra-k">View all my reviews</a>"""
    },
    {
        "date": "2023-07-18T12:00:00+00:00",
        "title": "Miles A. Drake - The Harrowing Deep",
        "file": "content/book/the_harrowing_deep.md",
        "tags": '["Fantasy", "Warhammer Age of Sigmar", "Short Stories"]',
        "html": """<a href="https://www.goodreads.com/book/show/51649461-the-harrowing-deep" style="float: left; padding-right: 20px"><img border="0" alt="The Harrowing Deep (Black Library Celebration 2020 #1)" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1582545959l/51649461._SY475_.jpg" /></a><a href="https://www.goodreads.com/book/show/51649461-the-harrowing-deep">The Harrowing Deep</a> by <a href="https://www.goodreads.com/author/show/17154659.Miles_A_Drake">Miles A. Drake</a><br/>
My rating: <a href="https://www.goodreads.com/review/show/5701931970">3 of 5 stars</a><br /><br />
A nice little short story, although this time it had a lot of words specific to the underwater world without much explanation (though understandably - if there was it would not be short). So for a short it was not an easy beginner-friendly read.
<br/><br/>
<a href="https://www.goodreads.com/review/list/163394279-david-stra-k">View all my reviews</a>"""
    },
    {
        "date": "2023-07-12T12:00:00+00:00",
        "title": "John French - Ahriman: Sorcerer",
        "file": "content/book/ahriman_sorcerer.md",
        "tags": '["Sci-Fi", "Warhammer 40k", "Fiction"]',
        "html": """<a href="https://www.goodreads.com/book/show/18775043-ahriman" style="float: left; padding-right: 20px"><img border="0" alt="Ahriman: Sorcerer (Ahriman #2)" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1407137924l/18775043._SY475_.jpg" /></a><a href="https://www.goodreads.com/book/show/18775043-ahriman">Ahriman: Sorcerer</a> by <a href="https://www.goodreads.com/author/show/6525693.John_French">John  French</a><br/>
My rating: <a href="https://www.goodreads.com/review/show/5593260273">5 of 5 stars</a><br /><br />
What a story!<br />This had me on my toes excited about what was to come all the time. With interesting characters and a great stroy, this is a book I'm really glad I started and finished.<br />Some of the negatives are that these ahriman stories seem to be little bit slower. And also this book did not feature ahriman that much, but nevertheless, it was epic and I'm glad I've read it.<br />Something is just so cool about the stuff that the characters can do, while it still makes sense from the set rules of the world.
<br/><br/>
<a href="https://www.goodreads.com/review/list/163394279-david-stra-k">View all my reviews</a>"""
    },
    {
        "date": "2023-07-11T12:00:00+00:00",
        "title": "Eric Gregory - The Warden in the Mountain",
        "file": "content/book/the_warden_in_the_mountain.md",
        "tags": '["Fantasy", "Warhammer Age of Sigmar", "Short Stories"]',
        "html": """<a href="https://www.goodreads.com/book/show/49406471-the-warden-in-the-mountain" style="float: left; padding-right: 20px"><img border="0" alt="The Warden in the Mountain (Warhammer Age of Sigmar)" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1569363804l/49406471._SY475_.jpg" /></a><a href="https://www.goodreads.com/book/show/49406471-the-warden-in-the-mountain">The Warden in the Mountain</a> by <a href="https://www.goodreads.com/author/show/1410414.Eric_Gregory">Eric Gregory</a><br/>
My rating: <a href="https://www.goodreads.com/review/show/5684477875">5 of 5 stars</a><br /><br />

<br/><br/>
<a href="https://www.goodreads.com/review/list/163394279-david-stra-k">View all my reviews</a>"""
    },
    {
        "date": "2023-06-20T12:00:00+00:00",
        "title": "John French - Ahriman: Gates of Ruin",
        "file": "content/book/ahriman_gates_of_ruin.md",
        "tags": '["Sci-Fi", "Warhammer 40k", "Short Stories"]',
        "html": """<a href="https://www.goodreads.com/book/show/23768283-ahriman" style="float: left; padding-right: 20px"><img border="0" alt="Ahriman: Gates of Ruin (Black Library Advent Calendar 2014 #15)" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1418648855l/23768283._SY475_.jpg" /></a><a href="https://www.goodreads.com/book/show/23768283-ahriman">Ahriman: Gates of Ruin</a> by <a href="https://www.goodreads.com/author/show/6525693.John_French">John  French</a><br/>
My rating: <a href="https://www.goodreads.com/review/show/5593262749">5 of 5 stars</a><br /><br />
A very well done and epic short story.<br />My favourite read of all the Ctesias short stories in the Ahriman omnibus.
<br/><br/>
<a href="https://www.goodreads.com/review/list/163394279-david-stra-k">View all my reviews</a>"""
    },
    {
        "date": "2023-06-17T12:00:00+00:00",
        "title": "John French - Ahriman: The First Prince",
        "file": "content/book/ahriman_the_first_prince.md",
        "tags": '["Sci-Fi", "Warhammer 40k", "Short Stories"]',
        "html": """<a href="https://www.goodreads.com/book/show/23381114-ahriman" style="float: left; padding-right: 20px"><img border="0" alt="Ahriman: The First Prince (Ahriman Audio Drama)" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1413448816l/23381114._SY475_.jpg" /></a><a href="https://www.goodreads.com/book/show/23381114-ahriman">Ahriman: The First Prince</a> by <a href="https://www.goodreads.com/author/show/6525693.John_French">John  French</a><br/>
My rating: <a href="https://www.goodreads.com/review/show/5593262719">5 of 5 stars</a><br /><br />
An interesting short story that finally goes less into Ctesias and more into Ahriman. Nevertheless it is a nice read and gives us more about the entourage of Ahriman on his quest.
<br/><br/>
<a href="https://www.goodreads.com/review/list/163394279-david-stra-k">View all my reviews</a>"""
    },
    {
        "date": "2023-06-17T12:00:00+00:00",
        "title": "John French - Hounds of Wrath",
        "file": "content/book/hounds_of_wrath.md",
        "tags": '["Sci-Fi", "Warhammer 40k", "Short Stories"]',
        "html": """<a href="https://www.goodreads.com/book/show/24762482-hounds-of-wrath" style="float: left; padding-right: 20px"><img border="0" alt="Hounds of Wrath" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1568232348l/24762482._SY475_.jpg" /></a><a href="https://www.goodreads.com/book/show/24762482-hounds-of-wrath">Hounds of Wrath</a> by <a href="https://www.goodreads.com/author/show/6525693.John_French">John  French</a><br/>
My rating: <a href="https://www.goodreads.com/review/show/5593262707">5 of 5 stars</a><br /><br />
A really good short story that is a prequel to the First Prince short story. This story went on really fast and to the point, but it still was interesting, even including plot twists.
<br/><br/>
<a href="https://www.goodreads.com/review/list/163394279-david-stra-k">View all my reviews</a>"""
    },
    {
        "date": "2023-06-17T12:00:00+00:00",
        "title": "Sandy Mitchell - Echoes of the Tomb",
        "file": "content/book/echoes_of_the_tomb.md",
        "tags": '["Sci-Fi", "Warhammer 40k", "Short Stories"]',
        "html": """<a href="https://www.goodreads.com/book/show/13560178-echoes-of-the-tomb" style="float: left; padding-right: 20px"><img border="0" alt="Echoes of the Tomb (Ciaphas Cain)" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1332686337l/13560178._SY475_.jpg" /></a><a href="https://www.goodreads.com/book/show/13560178-echoes-of-the-tomb">Echoes of the Tomb</a> by <a href="https://www.goodreads.com/author/show/217791.Sandy_Mitchell">Sandy Mitchell</a><br/>
My rating: <a href="https://www.goodreads.com/review/show/5620256949">3 of 5 stars</a><br /><br />
A nice little short story, although this one made me feel that Ciaphas really has plot armor and that is why he survives everything thrown at him.
<br/><br/>
<a href="https://www.goodreads.com/review/list/163394279-david-stra-k">View all my reviews</a>"""
    },
    {
        "date": "2023-06-17T12:00:00+00:00",
        "title": "Sandy Mitchell - For the Emperor",
        "file": "content/book/for_the_emperor.md",
        "tags": '["Sci-Fi", "Warhammer 40k", "Fiction"]',
        "html": """<a href="https://www.goodreads.com/book/show/709611.For_the_Emperor" style="float: left; padding-right: 20px"><img border="0" alt="For the Emperor (Ciaphas Cain, #1)" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1387744072l/709611._SY475_.jpg" /></a><a href="https://www.goodreads.com/book/show/709611.For_the_Emperor">For the Emperor</a> by <a href="https://www.goodreads.com/author/show/217791.Sandy_Mitchell">Sandy Mitchell</a><br/>
My rating: <a href="https://www.goodreads.com/review/show/5437369031">5 of 5 stars</a><br /><br />
The books about Ciaphas Cain are very different than usual warhammer books, but are very enjoyable nonetheless.<br />I personally love how he is of cowardly nature, but his deeds really are heroic, even though he does not feel like it.<br />I feel like these books are the greatest if you want warhammer stories that are not being told by big space marines. This story was more of a "normal guy tells you about his service in the military".
<br/><br/>
<a href="https://www.goodreads.com/review/list/163394279-david-stra-k">View all my reviews</a>"""
    },
    {
        "date": "2023-06-05T12:00:00+00:00",
        "title": "John French - Ahriman: The Dead Oracle",
        "file": "content/book/ahriman_the_dead_oracle.md",
        "tags": '["Sci-Fi", "Warhammer 40k", "Short Stories"]',
        "html": """<a href="https://www.goodreads.com/book/show/22672850-ahriman" style="float: left; padding-right: 20px"><img border="0" alt="Ahriman: The Dead Oracle (Ahriman)" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1404716535l/22672850._SY475_.jpg" /></a><a href="https://www.goodreads.com/book/show/22672850-ahriman">Ahriman: The Dead Oracle</a> by <a href="https://www.goodreads.com/author/show/6525693.John_French">John  French</a><br/>
My rating: <a href="https://www.goodreads.com/review/show/5593235327">4 of 5 stars</a><br /><br />
A pretty nice short story that fills the space and teaches us about the guy Ctesias and his skills.
<br/><br/>
<a href="https://www.goodreads.com/review/list/163394279-david-stra-k">View all my reviews</a>"""
    }
]

for b in books:
    # Use regex to grab the image URL properly and substitute dimensions
    img_match = re.search(r'src="([^"]+)"', b["html"])
    if img_match:
        old_url = img_match.group(1)
        new_url = re.sub(r'_(S[XY]\d+)_', '_SY475_', old_url)
        b["html"] = b["html"].replace(old_url, new_url)
        cover_image = new_url
    else:
        cover_image = ""
        
    content = f'''---
title: "{b['title']}"
date: "{b['date']}"
cover_image: "{cover_image}"
tags: {b['tags']}
---

{b['html']}'''
    with open(b["file"], "w") as f:
        f.write(content)
