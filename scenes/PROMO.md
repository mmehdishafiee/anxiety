# intro

`SceneSetup.intro();`

# intro-play-button

(...51)

[بازی!](#intro-start) `publish("intro-to-game-1"); Game.OVERRIDE_CHOICE_LINE=true;`

# intro-start

(...500)

`clearText()`

n3: قبل از اینکه شروع کنیم، بگو *دوست داری* چطور بخونی؟

`publish("show_options_bottom")`

# intro-start-2

n3: حالا بریم سراغ داستانمون...

```
publish("hide_tabs");
clearText();
```

(...1000)

`publish("intro-to-game-2")`

n2: این یه آدمه

(...600)

`clearText()`

(...300)

`publish("intro-to-game-3")`

# act1

```
SceneSetup.act1();
publish("hide_tabs");
music('battle', {volume:0.5});
```

(...300)

n: و این هم اضطرابِ این آدمه

n: _تو_ هستی که نقش اضطراب رو بازی می‌کنی

(#act1_normal)


# act1_normal

```
hong({body:"putaway"});
sfx("rustle");
Game.OVERRIDE_TEXT_SPEED = 1.5;
```

h: نه. نه، نه، گوش نمی‌دم. دارم گوشیمو چک می‌کنم.

```
sfx("rustle2");
hong({body:"phone1", mouth:"neutral", eyes:"neutral"})
```

n: وظیفه‌ات اینه که از آدمت در برابر *خطر* محافظت کنی

`bb({eyes:"look", mouth:"small_lock", body:"fear"})`

b: وای! داری بازم عمرتو تو توییتر هدر می‌دی!

```
bb({eyes:"normal", mouth:"normal", body:"normal"});
hong({eyes:"annoyed"});
```

h: آره، چه عجب که نمی‌شینم بیشتر به افکارم گوش بدم.

`hong({eyes:"neutral"});`

n: زود باش، بهش درباره‌ی یه *خطر* هشدار بده!

```
bb({eyes:"look"});
```

[اوه نه، ببین چه خبر وحشتناکی!](#act1d_news)

[اوه نه، این توییت داره مخفیانه درباره‌ی *ما* حرف می‌زنه؟](#act1d_subtweet)

[هی، یه گیف از یه گربه که شیر می‌خوره](#act1d_milk)

# act1d_milk

`hong({mouth:"smile", eyes:"surprise"});`

h: هه، آره نازه، من--

```
hong({mouth:"shock", eyes:"shock"});
bb({body:"scream"});
Game.OVERRIDE_TEXT_SPEED = 1.8;
```

b: گربه‌ها نمی‌تونن شیر رو هضم کنن و ما آدمای افتضاحی هستیم که از شکار حیوانات لذت می‌بریم

(...200)

```
bb({body:"normal", mouth:"normal", eyes:"fear"});
attack("20p", "bad");
publish("hp_show");
```
