# act1

`SceneSetup.act1();`

(...300)

n: و این هم اضطرابِ این آدمه

n: _تو_ هستی که نقش اضطراب رو بازی می‌کنی

{{if window.localStorage.continueChapter=="replay"}}
(#act1_replay)
{{/if}}

{{if window.localStorage.continueChapter!="replay"}}
(#act1_normal)
{{/if}}



# act1_replay

`hong({mouth:"0_neutral", eyes:"0_neutral"})`

h: اوه هی! برگشتیم اینجا؟

`hong({eyes:"0_neutral"})`

n: وظیفه‌ات اینه که از آدمت در برابر *خطر* محافظت کنی

`bb({eyes:"look", mouth:"small_lock"})`

n: در واقع، بازی کردنِ دوباره‌ی این بازی همین الان داره اون‌ها رو به *خطر* میندازه

n: زود باش، بهشون هشدار بده!

```
sfx("squeak");
bb({body:"squeeze_talk"});
hong({body:"0_squeeze"});
```

b: آدم! گوش کن، تو خطریم! بازیکن...

[...می‌خواد بازم شکنجه‌مون کنه!](#act1_replay_torture)

[...هیچ پایانِ دیگه‌ای پیدا نمی‌کنه!](#act1_replay_alternate)

[...به تناقضِ روایت-گیم‌پلی می‌رسه!](#act1_replay_dissonance)

# act1_replay_torture

```
window.HACK_REPLAY = JSON.parse(localStorage.act4);
bb({body:"normal", mouth:"normal", eyes:"fear"});
hong({body:"0_sammich"});
```

{{if window.HACK_REPLAY.act1_ending=="fight"}}
b: وادمون می‌کنه که مثل توپ جمع بشیم و گریه کنیم!
{{/if}}

{{if window.HACK_REPLAY.act1_ending=="flight"}}
b: وادمون می‌کنه گوشیمو بکشیم چون بهت حمله‌ی هراس داد!
{{/if}}

{{if window.HACK_REPLAY.a2_ending=="fight"}}
b: وادمون می‌کنه به میزبانِ مهمانی مشت *نزنیم*!
{{/if}}

{{if window.HACK_REPLAY.a2_ending=="flight"}}
b: وادمون می‌کنه به میزبانِ مهمانی که یه آنتی-ویلنِ دلسوزه مشت بزنیم!
{{/if}}

{{if window.HACK_REPLAY.a3_ending=="jump"}}
h: خب حداقل ممکنه این دفعه از پشت‌بام پرید نکنی--
{{/if}}

{{if window.HACK_REPLAY.a3_ending=="walkaway"}}
b: وادمون می‌کنه از پشت‌بام بپریم.
{{/if}}

`bb({body:"fear"});`

b: یه عالمه اتفاقِ وحشتناکِ جدید برامون میفته و بعد ما--

(#act1_replay_end)


# act1_replay_alternate

```
bb({body:"normal", mouth:"normal", eyes:"fear"});
hong({body:"0_sammich"});
```

h: بفرض، داستانِ *کلی* یکی می‌مونه، ولی هر فصل دو تا پایانِ ممکن داره، به‌علاوه‌ی همه‌ی شاخه‌های دیالوگ مختلف--

`bb({body:"fear"});`

b: بازیکن ناامید می‌شه، این تب رو می‌بنده، نرم‌افزارمون رو پاک می‌کنه و بعد ما--

(#act1_replay_end)


# act1_replay_dissonance

```
bb({body:"normal", mouth:"normal", eyes:"fear"});
hong({body:"0_sammich"});
```

h: تناقضِ-چی؟

`bb({eyes:"normal"});`

b: قوسِ داستانی درباره‌ی این بود که می‌تونی انتخاب کنی که با ترست یه همکاریِ سالم بسازی،

`bb({eyes:"normal_right"});`

b: ولی دوباره بازی کردنش همون داستان رو نشون می‌ده، یعنی انگار *انتخاب*‌هات هیچ اهمیتی نداشتن،

`bb({eyes:"narrow_eyebrow"});`

b: پس یه تناقض بین پیامِ بازی و مکانیک‌هاش به وجود میاد،

`bb({eyes:"fear"});`

b: و این‌طوری بافتِ این جهانِ داستانی از هم می‌گسله،

`bb({body:"fear"});`

b: و بعد ما--

(#act1_replay_end)


# act1_replay_end

`bb({body:"panic"})`

b: بمییییییییییییییییر

```
bb({body:"normal", mouth:"normal", eyes:"normal"});
Game.clearText();
```

(...1001)

```
bb({body:"laugh"});
hong({body:"laugh"});
Game.clearText();
sfx("laugh");
```

(...5001)

```
bb({body:"normal", mouth:"normal", eyes:"normal"});
hong({body:"0_sammich"});
```

h: خب بریم سراغ نقش‌هامون.

```
Game.clearText();
```

n4: (بگذار اضطرابِ _خودت_ بله بله بله شبیه‌ترین به چیزی که _ترس_‌هات بله بله بله می‌دونی که چی می‌گم)

```
sfx("squeak");
hong({body:"0_squeeze"});
bb({body:"squeeze"});
```

(#act1_normal_choice)



# act1_normal

`hong({mouth:"0_neutral", eyes:"0_annoyed"})`

h: اوه عالی، گرگم برگشته. چه عاااالی.

`hong({eyes:"0_neutral"})`

n: وظیفه‌ات اینه که از آدمت در برابر *خطر* محافظت کنی

`bb({eyes:"look", mouth:"small_lock"})`

n: در واقع، اون ساندویچ همین الان داره اون‌ها رو به *خطر* میندازه

n: زود باش، بهشون هشدار بده!

```
sfx("squeak");
bb({body:"squeeze_talk"});
hong({body:"0_squeeze"});
```

b: آدم! گوش کن، تو خطریم! خطرش اینه که...

`bb({body:"squeeze"})`

n4: (بگذار اضطرابِ _خودت_ بیاد بازی کنه! چیزی رو انتخاب کن که بیشتر شبیه حرفِ _ترس_‌های خودته)

(#act1_normal_choice)

# act1_normal_choice

[داریم ناهار رو تنهایی می‌خوریم! بازم!](#act1a_alone) `bb({body:"squeeze_talk"})`

[موقع غذا خوردن هیچ کاری پیش نمی‌بریم!](#act1a_productive) `bb({body:"squeeze_talk"})`

[اون نونِ سفید به ضررمونه!](#act1a_bread) `bb({body:"squeeze_talk"})`

# act1a_alone

```
bb({body:"normal", mouth:"small", eyes:"narrow"});
hong({body:"0_sammich"});
```

b: نمی‌دونی تنهایی به همون اندازه‌ی روزی ۱۵ نخ سیگار کشیدن با مرگ زودرس مرتبطه؟-

`Game.OVERRIDE_TEXT_SPEED = 2;`

`bb({mouth:"normal", eyes:"normal_right"})`

b: (هولت-لونستاد ۲۰۱۰، PLoS Medicine)

`hong({eyes:"0_annoyed"})`

h: مم، ممنون که منابعت رو ذکر کردی ولی--

`Game.OVERRIDE_TEXT_SPEED = 2;`

`bb({body:"fear", mouth:"normal", eyes:"fear"})`

b: یعنی اگه همین الان با کسی بیرون نریم داریم--

`bb({body:"panic"})`

b: میمییییییییییییییییییریم

```
bb({body:"normal", mouth:"normal", eyes:"normal"});
hong({mouth:"0_shock", eyes:"0_shock"});
attack("18p", "alone");
publish("hp_show");
```

(...2500)

`_.fifteencigs = true`

n: *ترس از دوست‌نداشته‌شدن* رو به کار گرفتی

(#act1b)

# act1a_productive

```
bb({body:"normal", mouth:"small", eyes:"normal"});
hong({body:"0_sammich"});
```

b: لپ‌تاپتو دربیار و همین الان یه کاری بکن!

`hong({eyes:"0_annoyed"})`

h: مم، ترجیح می‌دم خرده‌های نون نره توی کیبوردم--

```
bb({mouth:"normal", eyes:"fear"});
Game.OVERRIDE_TEXT_SPEED = 1.5;
```

b: اگه به بدنِ جامعه کمک نکنیم یعنی ما یه انگلِ جامعه‌ایم!

b: بدنِ جامعه می‌ره پیش دکترِ جامعه تا دارویی بگیره که انگل‌های جامعه‌ش رو بکشه و بعد ما--

```
bb({body:"panic", mouth:"normal", eyes:"fear"});
Game.OVERRIDE_TEXT_SPEED = 1.5;
```

b: میمییییییییییییییییییریم

```
bb({body:"normal", mouth:"normal", eyes:"normal"});
hong({mouth:"0_shock", eyes:"0_shock"});
attack("18p", "bad");
publish("hp_show");
```

(...2500)

`_.parasite = true`

n: *ترس از آدمِ‌بد بودن* رو به کار گرفتی

(#act1b)

# act1a_bread

```
bb({body:"normal", mouth:"normal", eyes:"fear"});
hong({body:"0_sammich", eyes:"0_annoyed"});
```

h: اون تحقیق‌ها تکرارپذیری شدن؟--

```
bb({body:"fear", mouth:"normal", eyes:"fear"});
Game.OVERRIDE_TEXT_SPEED = 1.5;
```

b: گندمِ فرآوری‌شده قند خونمون رو بالا می‌بره و مجبور می‌شن همه‌ی دست‌وپاهامون رو قطع کنن و بعد ما--

`bb({body:"panic"})`

b: میمییییییییییییییییییریم

```
bb({body:"normal", mouth:"normal", eyes:"normal"});
hong({mouth:"0_shock", eyes:"0_shock"});
attack("18p", "harm");
publish("hp_show");
```

(...2500)

`_.whitebread = true`

n: *ترس از آسیب‌دیدن* رو به کار گرفتی

(#act1b)

# act1b

n: فوق‌العاده مؤثر بود!

`bb({mouth:"smile", eyes:"smile"});`

b: دیدی آدم؟ من گرگِ نگهبانِ وفادارتم!

`bb({body:"pride_talk"});`

b: به شهودت اعتماد کن! احساساتت همیشه معتبرن!

`bb({body:"pride"});`

n: نوارِ انرژیِ آدمت رو به صفر برسون

n: برای محافظت از نیازهای فیزیکی + اجتماعی + اخلاقیش می‌تونی از این‌ها استفاده کنی:

n: ترس از *آسیب‌دیدن* #harm#

n: ترس از *دوست‌نداشته‌شدن* #alone#

n: و ترس از *آدمِ‌بد بودن* #bad#

`Game.OVERRIDE_TEXT_SPEED = 1.25;`

n4: (نکته‌ی حرفه‌ای: انتخاب‌هایی رو بازی کن که شخصاً به عمیق‌ترین و تاریک‌ترین ترس‌هات می‌خورن!~)

h: ...

```
hong({body:"putaway"});
sfx("rustle");
bb({body:"normal", mouth:"normal", eyes:"normal"});
```

(...1000)

`Game.OVERRIDE_TEXT_SPEED = 1.5;`

h: می‌دونی چیه شاید وقتشه گوشیمو چک کنم.

```
sfx("rustle2");
hong({body:"phone1", mouth:"neutral", eyes:"neutral"})
```

n: از آدمت محافظت کن

n: از دنیا. از بقیه. از خودش.

n: موفق باشی

(...500)

`Game.clearText()`

(...500)

(#act1c)

# act1c

`music('battle', {volume:0.5})`

n: راند یک: *جنگ!*

`bb({body:"normal", mouth:"normal", eyes:"normal"});`

h: هه. فید فیس‌بوک می‌گه آخر هفته یه مهمانی هست.

`bb({eyes:"uncertain"});`

b: اون عجق‌وجق هر آخر هفته مهمانی نمی‌گیره؟

`bb({eyes:"uncertain_right"});`

b: داره چه خلأ درونی‌ای رو پر می‌کنه؟ حتماً از داخل حسابی خرابه!

`hong({eyes:"surprise"});`

h: ضمناً، من دعوت شدم؟

`bb({eyes:"fear", mouth:"normal"});`

b: پس عالی شد!

[بگو بله، وگرنه از تنهایی می‌میریم!](#act1c_loner)

[بگو نه، پر از موادِ سمیه!](#act1c_drugs)

[بیخیالش شو، ما فقط مهمانی‌ها رو غمگین می‌کنیم.](#act1c_sad)

# act1c_loner

{{if _.fifteencigs}}
b: روزی پونزده نخ سیگار، آدم! پونزده تا!
{{/if}}

{{if !_.fifteencigs}}
`Game.OVERRIDE_TEXT_SPEED = 1.5;`
{{/if}}

{{if !_.fifteencigs}}
b: اون‌وقت هیچ‌کس تو مراسم خاک‌سپاریمون شرکت نمی‌کنه، خاکسترمون رو می‌ریزن تو دریا، یه نهنگ می‌خورتمون،
{{/if}}

{{if !_.fifteencigs}}
b: و تبدیل به مدفوعِ نهنگ می‌شیم!
{{/if}}

{{if !_.fifteencigs}} `_.whalepoop = true` {{/if}}

(...500)

```
hong({mouth:"shock", eyes:"shock"});
attack("18p", "alone");
```

(...2500)

`bb({eyes:"normal"});`

{{if !_.fifteencigs}}
b: پس آره باید بریم اون مهمانی!
{{/if}}

{{if _.parasite}}
b: فقط لپ‌تاپ رو بیار که بتونیم کار کنیم و انگلِ جامعه نباشیم.
{{/if}}

{{if _.whitebread}}
b: فقط به شرطی که نونِ سفید سرو نکنن
{{/if}}

`hong({mouth:"anger", eyes:"anger"});`

h: خدایا. اگه باعث بشه دهنت رو ببندی، باشه.

h: می‌گم بله.

{{if _.whalepoop}}
b: مدفوع نهنگ، آدم! مدفوع نهنگ!
{{/if}}

`_.partyinvite="yes"`

(#act1d)

# act1c_drugs

`bb({mouth:"small", eyes:"fear"});`

{{if _.whitebread}}
b: یا حتی بدتر... نونِ سفید
{{/if}}

{{if _.whitebread}}
`Game.OVERRIDE_TEXT_SPEED = 1.5;`
{{/if}}

{{if _.whitebread}}
b: از انقدر شیشه و نونِ سفید اوردوز می‌کنیم که جسدِ چاقمون تو کوره‌ی سوزاندن جا نمی‌شه!
{{/if}}

{{if !_.whitebread}}
b: از انقدر مواد اوردوز می‌کنیم که مُرده‌شور فکر می‌کنه بدنمون از قبل مومیایی شده!
{{/if}}

```
hong({mouth:"shock", eyes:"shock"});
attack("18p", "harm");
```

(...2500)

{{if _.parasite}}
b: ضمناً، نمی‌تونیم مهمانی بریم، باید کار کنیم وگرنه انگلِ جامعه‌ایم!
{{/if}}

`hong({mouth:"anger", eyes:"anger"});`

h: خدایا. اگه باعث بشه دهنت رو ببندی، باشه.

h: می‌گم نه.

`_.partyinvite="no"`

(#act1d)

# act1c_sad

`bb({eyes:"uncertain_right", mouth:"normal"});`

`Game.OVERRIDE_TEXT_SPEED = 1.5;`

{{if _.fifteencigs}}
b: تنها کاری که همیشه می‌کنیم اینه که تو یه گوشه گریه کنیم که تنهایی به اندازه‌ی روزی ۱۵ نخ سیگار کشنده‌ست.
{{/if}}

{{if _.parasite}}
b: تنها کاری که تو مهمانی‌ها می‌کنیم اینه که نگران باشیم باید به جاش کار می‌کردیم.
{{/if}}

{{if _.whitebread}}
b: تنها کاری که می‌کنیم اینه که نگران باشیم غذاهای ناسالم قراره بکشتمون.
{{/if}}

```
bb({mouth:"normal", eyes:"normal"});
hong({mouth:"neutral", eyes:"lookaway"});
```

h: هوم عجب، چرا حدس نمی‌زنم.

`hong({eyes:"neutral"});`

`Game.OVERRIDE_TEXT_SPEED = 1.5;`

b: پس اگه بریم حالشون رو می‌گیریم، ولی اگه دعوتشون رو رد کنیم بازم حالشون رو می‌گیریم!

`bb({body:"fear", eyes:"fear"});`

`Game.OVERRIDE_TEXT_SPEED = 1.5;`

b: ما همیشه فقط حالِ آدم‌ها رو می‌گیریم، پس باید حالمون بد بشه

```
hong({mouth:"shock", eyes:"shock"});
attack("18p", "bad");
```

(...2500)

`hong({mouth:"anger", eyes:"anger"});`

h: اوف. اگه باعث بشه دهنت رو ببندی، باشه.

h: دعوت رو نادیده می‌گیرم.

`_.partyinvite="ignore"`

(#act1d)

# act1d

```
bb({body:"normal", mouth:"normal", eyes:"normal"});
hong({mouth:"neutral", eyes:"annoyed"});
```

h: به هر حال. فیس‌بوک زیادیه. یه چیز آروم‌تر می‌خوام، کمتر اضطراب‌ساز.

`hong({eyes:"neutral"});`

h: تو توییتر چه خبره؟

`bb({eyes:"look"});`

[اوه نه، ببین چه خبر وحشتناکی!](#act1d_news)

[اوه نه، این توییت داره مخفیانه درباره‌ی *ما* حرف می‌زنه؟](#act1d_subtweet)

[هی، یه گیف از یه گربه که شیر می‌خوره](#act1d_milk)


# act1d_news

```
bb({eyes:"pained1"});
music(null, {fade:2});
```

b: خدایا، انگار دنیا داره می‌سوزه، نه؟

```
bb({eyes:"pained2"});
hong({mouth:"sad", eyes:"sad"});
```

b: انگار همه‌چیز داره تموم می‌شه، انگار همه‌چیز داره می‌میره و کارش داشتنیم و هیچ کاری از دستمون برنمیاد.

```
Game.OVERRIDE_TEXT_SPEED = 0.5;
bb({mouth:"shut"});
```

b: ...

`bb({mouth:"smile", eyes:"smile"});`

b: بریم اون خبر رو ریتوییت کنیم!

```
hong({mouth:"shock", eyes:"shock"});
attack("18p", "harm");
```

(...2500)

`_.badnews=true`

```
music('battle', {volume:0.5});
hong({mouth:"anger", eyes:"anger"});
bb({body:"normal", mouth:"normal", eyes:"normal"});
Game.OVERRIDE_TEXT_SPEED = 1.5;
```

h: باشه ریتوییتش می‌کنم فقط لطفاً ساکت شو!

`hong({mouth:"neutral", eyes:"annoyed"});`

h: ولش کن، بریم اسنپ‌چت رو ببینیم.

(#act1e)


# act1d_subtweet

`bb({eyes:"fear"});`

b: ساب‌توییته! یه ساب‌توییتِ شیطونِ شیطون!

`hong({eyes:"annoyed"});`

h: احتمالاً نیست؟

`bb({eyes:"narrow", mouth:"small"});`

b: ولی اگه همه دارن پشت سرمون حرف می‌زنن

h: نمی‌زن--

`bb({body:"fear", eyes:"fear", mouth:"normal"});`

b: جلوی پشت‌مون

`hong({eyes:"sad", mouth:"sad"});`

h: من نمی‌--

`bb({eyes:"narrow", mouth:"small"});`

b: ولی *اگه*

h: م--

`bb({eyes:"narrow_eyebrow"});`

b: *اگه*

```
Game.OVERRIDE_TEXT_SPEED = 0.5;
hong({mouth:"shut"});
```

h: ...

(...1000)

```
hong({mouth:"shock", eyes:"shock"});
attack("18p", "alone");
```

(...2500)

`_.subtweet=true`

```
hong({mouth:"anger", eyes:"annoyed"});
bb({body:"normal", mouth:"normal", eyes:"normal"});
```

h: ب-اشه، دارم می‌رم اسنپ‌چت.

(#act1e)

# act1d_milk

`hong({mouth:"smile", eyes:"neutral"});`

h: هه آره نازه، همین الانم ریتوییت کردم، فکر کن--

```
hong({mouth:"shock", eyes:"shock"});
bb({body:"scream"});
Game.OVERRIDE_TEXT_SPEED = 1.8;
```

b: گربه‌ها نمی‌تونن شیر رو هضم کنن و ما آدمای افتضاحی هستیم که از شکار حیوانات لذت می‌بریم

```
bb({body:"normal", mouth:"normal", eyes:"fear"});
attack("18p", "bad");
```

(...2500)


`_.catmilk=true`

```
hong({mouth:"anger", eyes:"annoyed"});
bb({body:"normal", mouth:"normal", eyes:"normal"});
```

h: ب-اشه، دارم می‌رم اسنپ‌چت.

(#act1e)

# act1e

`hong({mouth:"neutral", eyes:"neutral"});`

h: هوم، عکس‌های دیشبه. پس مهمانی‌های هفتگی این‌طورین.

{{if _.partyinvite=="yes"}} (#act1e_said_yes) {{/if}}

{{if _.partyinvite=="no"}} (#act1e_said_no) {{/if}}

{{if _.partyinvite=="ignore"}} (#act1e_said_ignore) {{/if}}

# act1e_said_yes

`hong({mouth:"sad", eyes:"annoyed"});`

h: اوف، خیلی شلوغه برای اضطرابم.

h: شاید نباید به دعوت می‌گفتم بله؟

```
hong({mouth:"neutral", eyes:"neutral"});
bb({mouth:"normal", eyes:"normal"});
```

[جوابمون رو عوض کنیم؟ مثل بی‌ادبا؟!](#act1e_yes_dontchange)

[جوابمون رو عوض کنیم! خیلی شلوغه!](#act1e_yes_changetono)

{{if _.subtweet}}
[آره، دقیقاً داشتن ساب‌توییت ما می‌کردن.](#act1e_ignore_subtweet)
{{/if}}

{{if _.badnews}}
[صبر کن ما بدون فکت-چک ریتوییت کردیم.](#act1e_ignore_factcheck)
{{/if}}

{{if (!_.subtweet && !_.badnews)}}
[می‌دونی، وضعیت نشستنت خیلی بده؟](#act1e_ignore_posture)
{{/if}}

# act1e_yes_dontchange

```
bb({eyes:"anger"});
Game.OVERRIDE_TEXT_SPEED = 1.5;
```

b: رو ما حساب می‌کردن که بیایم و حالا داریم به اعتمادشون خیانت می‌کنیم؟ می‌خوای تنها بمیری؟!

{{if _.fifteencigs}}
b: پونزده. نخ. سیگار.
{{/if}}

{{if _.whalepoop}}
b: مدفوع. نهنگ.
{{/if}}

```
hong({mouth:"shock", eyes:"shock"});
attack("18p", "alone");
```

(...2500)

```
hong({mouth:"anger", eyes:"anger"});
Game.OVERRIDE_TEXT_SPEED = 1.5;
```

h: خفه شو خفه شو جواب رو بله نگه می‌دارم!

(#act1f)

# act1e_yes_changetono

```
bb({eyes:"fear"});
Game.OVERRIDE_TEXT_SPEED = 1.5;
```

b: از هولِ انسانی چیزی نمی‌دونی؟

```
bb({body:"fear", mouth:"small", eyes:"narrow"});
hong({eyes:"sad", mouth:"sad"});
Game.OVERRIDE_TEXT_SPEED = 1.5;
```

b: تو سال ۲۰۰۳ یه کلوب شبانه تو رود آیلند آتیش گرفت و وحشت باعث شد آدم‌ها تو خروجی‌ها گیر کنن و ۱۰۰ نفر سوختن و مُردن-

```
bb({body:"normal", mouth:"normal", eyes:"fear"});
hong({mouth:"shock"});
Game.OVERRIDE_TEXT_SPEED = 1.5;
```

b: می‌خوای همون اتفاق واسه ما بیفته-

```
bb({body:"scream"});
Game.OVERRIDE_TEXT_SPEED = 2.5;
```

b: بگو نه بگو نه بگو نه بگو نه بگو نه بگو نه بگو نه بگو نه بگو ن-


```
bb({body:"normal", eyes:"fear", mouth:"normal"});
hong({mouth:"shock", eyes:"shock"});
attack("18p", "harm");
```

(...2500)

```
hong({eyes:"anger", mouth:"anger"});
Game.OVERRIDE_TEXT_SPEED = 1.5;
```

h: خفه شو خفه شو جواب رو می‌کنم نه! خدایا!

(#act1f)

# act1e_said_no

`hong({mouth:"sad", eyes:"sad"});`

h: هوم... خیلی بامزه به نظر می‌رسه.

h: شاید نباید به دعوت می‌گفتم نه؟

`bb({mouth:"normal", eyes:"normal"});`

[جوابمون رو عوض کنیم؟ مثل بی‌ادبا؟!](#act1e_no_dontchange)

[جوابمون رو عوض کنیم! تنها نمیریم!](#act1e_no_changetoyes)

{{if _.subtweet}}
[آره، دقیقاً داشتن ساب‌توییت ما می‌کردن.](#act1e_ignore_subtweet)
{{/if}}

{{if _.badnews}}
[صبر کن ما بدون فکت-چک ریتوییت کردیم.](#act1e_ignore_factcheck)
{{/if}}

{{if (!_.subtweet && !_.badnews)}}
[می‌دونی، وضعیت نشستنت خیلی بده؟](#act1e_ignore_posture)
{{/if}}

# act1e_no_dontchange

`bb({eyes:"anger"})`

b: همه رو ما حساب می‌کردن!

b: ...که تنها بمونیم و بذاریم یه مهمانیِ خوب بدون یه موجودِ ترسناکِ {{if _.whitebread}}نان‌سفید-خور{{/if}} مثل ما داشته باشن--


```
hong({mouth:"shock", eyes:"shock"});
attack("18p", "bad");
```

(...2500)

```
bb({body:"normal", eyes:"uncertain", mouth:"normal"});
hong({mouth:"anger", eyes:"anger"});
Game.OVERRIDE_TEXT_SPEED = 1.5;
```

h: خفه شو خفه شو جواب رو نه نگه می‌دارم!

(#act1f)

# act1e_no_changetoyes

```
bb({body:"fear", eyes:"fear", mouth:"normal"});
Game.OVERRIDE_TEXT_SPEED = 1.5;
```

b: تنهاییِ مزمن سطح کورتیزولمون رو بالا می‌بره و خطر بیماری قلبی-عروقی و سکته رو زیاد می‌کنه!

```
hong({mouth:"shock", eyes:"shock"});
attack("18p", "harm");
```

(...2500)

{{if _.fifteencigs}}
b: پونزده. نخ. سیگار.
{{/if}}

```
bb({body:"normal", eyes:"normal", mouth:"normal"});
hong({mouth:"anger", eyes:"anger"});
Game.OVERRIDE_TEXT_SPEED = 1.5;
```

h: خفه شو خفه شو جواب رو می‌کنم بله! خدایا!

(#act1f)

# act1e_ignore_subtweet

```
bb({eyes:"fear", mouth:"small"});
Game.OVERRIDE_TEXT_SPEED = 1.5;
```

b: همه‌ی توییت‌های مشکل‌سازمون برگشتن که دمار از روزگارمون دربیارن!

```
bb({body:"fear", eyes:"fear", mouth:"normal"});
Game.OVERRIDE_TEXT_SPEED = 1.7;
```

b: صدامون می‌زنن، کنسلمون می‌کنن و با طناب و اسب در بزرگراه اطلاعاتی می‌کشنمون!

```
hong({mouth:"shock", eyes:"shock"});
attack("18p", "alone");
```

(...2500)

```
bb({body:"normal", eyes:"normal", mouth:"normal"});
hong({mouth:"anger", eyes:"anger"});
Game.OVERRIDE_TEXT_SPEED = 1.5;
```

h: تو چرا این‌طوری هستی؟!

(#act1f)

# act1e_ignore_factcheck

```
bb({eyes:"fear"});
Game.OVERRIDE_TEXT_SPEED = 1.5;
```

b: داریم اطلاعاتِ نادرست پخش می‌کنیم! داریم اعتماد به مطبوعاتِ آزاد رو نابود می‌کنیم!

```
bb({body:"scream"});
Game.OVERRIDE_TEXT_SPEED = 1.5;
```

b: ما دلیلِ اینیم که فاشیسم از خرابه‌های دموکراسی بلند می‌شه!

```
bb({body:"normal", eyes:"anger"});
hong({mouth:"shock", eyes:"shock"});
attack("18p", "bad");
```

(...2500)

```
hong({mouth:"anger", eyes:"anger"});
Game.OVERRIDE_TEXT_SPEED = 1.5;
_.factcheck = true;
```

h: تو چرا این‌طوری هستی؟!

(#act1f)

# act1e_ignore_posture

```
bb({eyes:"fear"});
Game.OVERRIDE_TEXT_SPEED = 1.5;
```

b: می‌خوای ستون فقراتت مثل پرتزل بشه؟! دمِ مانیتور قوز نکن!

```
bb({body:"meta"});
```

b: تو هم همین‌طور.

```
bb({body:"normal", mouth:"normal"});
hong({mouth:"shock", eyes:"shock"});
attack("18p", "harm");
```

(...2500)

```
bb({body:"normal", eyes:"normal", mouth:"normal"});
hong({mouth:"anger", eyes:"anger"});
Game.OVERRIDE_TEXT_SPEED = 1.5;
```

h: تو چرا این‌طوری هستی؟!

(#act1f)

# act1e_said_ignore

`hong({mouth:"sad", eyes:"sad"});`

h: هوم... خیلی بامزه به نظر می‌رسه.

h: شاید نباید دعوت رو نادیده می‌گرفتم؟

`bb({mouth:"normal", eyes:"normal"});`

[به نادیده گرفتن ادامه بده، ما هنوز کس‌خل هستیم.](#act1e_ignore_continue)

[راستش، بگو بله.](#act1e_ignore_changetoyes)

[راستش، بگو نه.](#act1e_ignore_changetono)

# act1e_ignore_continue

`hong({eyes:"annoyed"});`

h: یه جورایی بی‌ادبانه‌ست که بازم نادیده‌شون بگیریم، نه؟

`bb({eyes:"normal_right"});`

b: خب بقیه همیشه *ما* رو نادیده می‌گیرن، پس

```
hong({mouth:"shock", eyes:"shock"});
attack("18p", "alone");
```

(...2500)

`bb({eyes:"normal"});`

b: پس بذار حسابمون رو تسویه کنیم.

(#act1f)

# act1e_ignore_changetoyes

`hong({eyes:"surprise", mouth:"smile"});`

h: داری... بهم اجازه‌ی خوش گذروندن می‌دی؟

b: خب، یعنی، تنهایی *می‌تونه* بکشتمون.

`hong({eyes:"neutral", mouth:"neutral"});`

(#act1e_no_changetoyes)

# act1e_ignore_changetono

`bb({eyes:"narrow"});`

b: خیلی شلوغه. جمعیت خطرناکه.

(#act1e_yes_changetono)


# act1f

```
bb({body:"normal", mouth:"normal", eyes:"normal"});
hong({mouth:"neutral", eyes:"neutral"});
```

h: هر کی هست. یه نوتیفیکیشن تیندر اومد.

`bb({eyes:"uncertain"})`

b: چی، اون اپ سکس‌یابی؟

`hong({eyes:"annoyed"})`

h: سکس‌یابی نیست، فقط یه راهه که با آدمای جدید آشنا بشی--

`bb({eyes:"narrow"})`

b: اپ سکس‌یابیه.

```
hong({eyes:"surprise", mouth:"smile"});
bb({eyes:"normal"});
```

h: اوه، مچ شدم! ناز به نظر می‌رسن!

```
bb({eyes:"narrow_eyebrow"});
hong({eyes:"sad", mouth:"anger"})
```

h: لطفاً اینو هم برام خراب نک--

```
bb({body:"panic"});
Game.OVERRIDE_TEXT_SPEED = 2.0;
```

b: خطر خطر خطر خطر خطر خطر

`bb({body:"fear", eyes:"fear", mouth:"normal"})`

[بقیه دارن از ما *استفاده* می‌کنن.](#act1f_used_by_others)

[ما داریم از بقیه *استفاده* می‌کنیم.](#act1f_using_others)

[مچِ تو یه قاتلِ سریالیه](#act1f_killer)

# act1f_used_by_others

`bb({body:"point_crotch", eyes:"normal", mouth:"normal"})`

b: سکس‌های تصادفی شاید بتونن اون حفره‌ی اون‌پایین رو پر کنن،

b: ولی هیچ‌وقت نمی‌تونن حفره‌ی...

`bb({body:"point_heart", eyes:"pretty", mouth:"small"})`

b: *اینجا* رو پر کنن.

(...1000)

```
bb({body:"normal", mouth:"normal", eyes:"fear"});
Game.OVERRIDE_TEXT_SPEED = 1.5;
```

b: نکته اینه که ما تنها می‌میریم

```
hong({mouth:"shock", eyes:"shock"});
attack("18p", "alone");
```

(...2500)

`_.hookuphole=true`

(#act1g)

# act1f_using_others

`bb({eyes:"narrow", mouth:"small"})`

b: فکر می‌کنی آلتِ آدما پوکمونن که جمع‌اشون کنیم؟

```
bb({body:"sing", eyes:"pretty", mouth:"shut"});
music("pokemon");
Game.clearText();
Game.FORCE_CANT_SKIP = true;
```

```
Game.FORCE_TEXT_DURATION = 1000;
Game.FORCE_NO_VOICE = true;
```

b: ♫ (آهنگِ پوکمون)-

(...5600)

```
bb({mouth:"normal"});
Game.FORCE_TEXT_DURATION = 2400;
```

b: ♫ می‌خوام من، ^فاحشه‌-ترین^ بشم-

(...500)

```
bb({eyes:"narrow", mouth:"small"});
Game.FORCE_TEXT_DURATION = 2100;
```

b: ♫ مثل هیچ‌کس نشده تا حالا-

(...1500)

```
bb({eyes:"pretty"});
Game.FORCE_TEXT_DURATION = 2300;
```

b: ♫ ران و ^کون^، سینه‌های برجسته-

(...500)

```
bb({eyes:"fear", mouth:"normal"});
Game.FORCE_TEXT_DURATION = 2000;
```

b: ♫ با ^کیر^ و بیضه‌های عرق‌کرده!-

(...1000)

```
bb({eyes:"smile", mouth:"smile"});
Game.FORCE_TEXT_DURATION = 1000;
```

b: ♫ منحرفمون! همه رو جم-

```
Game.FORCE_CANT_SKIP = false;
Game.clearText();
music(false);
bb({body:"normal", mouth:"normal", eyes:"normal"});
Game.OVERRIDE_TEXT_SPEED = 1.5;
```

b: نکته اینه که ما یه موجودِ ترسناکِ بازیگوشیم.

```
hong({mouth:"shock", eyes:"shock"});
attack("18p", "bad");
```

(...2500)

`_.pokemon=true`

(#act1g)

# act1f_killer

`Game.OVERRIDE_TEXT_SPEED = 1.5;`

{{if _.whitebread}}
b: می‌گیرتت تو چاه و زورکی نون سفید بهت می‌خورونن که چاق بشی و پوستتو بپوشن!
{{/if}}

{{if _.parasite}}
b: با تایمرِ پومودورو بهت می‌کوبن و می‌گن «باید بیشتر کار می‌کردی انگلِ لامصب»
{{/if}}

{{if !_.whitebread && !_.parasite}}
b: گوشتو می‌درده به تکه‌های خونی، روده‌هات رو می‌کنه روبان، و خونت رو می‌ریزه تو کاسه‌ی پانچ!
{{/if}}

{{if !_.whitebread && !_.parasite}}
b: این چطور برای یه دعوتِ مهمانی؟!
{{/if}}

```
hong({mouth:"shock", eyes:"shock"});
attack("18p", "harm");
```

(...2500)

`_.serialkiller=true`

(#act1g)

# act1g

```
bb({body:"normal", mouth:"normal", eyes:"look"});
hong({body:"2_tired"});
Game.OVERRIDE_TEXT_SPEED = 0.5;
music(false);
```

h: ...

(...500)

h: دیگه از این بازی دارم حالم به‌هم می‌خوره.

(...700)

`Game.OVERRIDE_TEXT_SPEED = 1.5;`

h:
{{if _.fifteencigs}}«تنهایی بکشتمونه»... {{/if}}
{{if _.parasite}}«ما انگلِ جامعه‌ایم»... {{/if}}
{{if _.whitebread}}«اونو نخور، بکشتمونه»... {{/if}}
{{if _.subtweet}}«دارن پشت سرمون حرف می‌زنن»... {{/if}}
{{if _.badnews}}«دنیا داره می‌سوزه»... {{/if}}
{{if _.hookuphole}}«تنها می‌میریم»... {{/if}}
{{if _.serialkiller}}«اونا قاتل سریالین»... {{/if}}
{{if _.catmilk}}«گربه‌ها نمی‌تونن شیر رو هضم کنن»... {{/if}}
{{if _.pokemon}}یه آهنگِ ^مزخرفِ^ تقلبی... {{/if}}

h: من فقط می‌خوام زندگیم رو بکنم.

h: من فقط می‌خوام از همه‌ی این... درد رها بشم.

`bb({eyes:"look_sad"});`

b: هی... آدم...

`Game.OVERRIDE_TEXT_SPEED = 0.5;`

b: درست می‌شه.

(...600)

`bb({body:"point_heart", eyes:"look_sad_smile", mouth:"smile"});`

b: به‌عنوان گرگِ نگهبانِ وفادارت، همیشه دنبال خطر می‌گردم، و تمام تلاشم رو می‌کنم که امنیتت رو حفظ کنم.

`bb({body:"normal", eyes:"look_sad", mouth:"smile"});`

b: قول می‌دم.

(...600)

```
bb({body:"normal", eyes:"normal", mouth:"normal"});
hong({body:"phone1", eyes:"neutral", mouth:"neutral"});
```

h: آخرین اپ. اینستاگرام. چی داری؟

`hong({eyes:"sad"});`

h: ...باز عکس مهمانیه.

`hong({mouth:"sad"});`

h: همه انقدر خوشحالن. از نگرانی راحت. از اضطراب راحت.

`hong({mouth:"anger"});`

h: خدایا، چرا نمی‌تونم مثل اونا باشم؟ چرا نمی‌تونم فقط *عادی* باشم؟

`bb({eyes:"normal_right"});`

b: در رابطه با مهمانی‌ها، در مورد دعوتِ این آخر هفته. اینم تصمیمِ نهاییِ من:

`bb({eyes:"normal"});`

[باید بریم.](#act1g_go) `Game.OVERRIDE_CHOICE_LINE=true`

[نباید بریم.](#act1g_dont) `Game.OVERRIDE_CHOICE_LINE=true`

# act1g_go

`_.act1g = "go"`

(#act1h)

# act1g_dont

`_.act1g = "dont"`

(#act1h)

# act1h

b: ما با--

```
bb({eyes:"wat", mouth:"small"});
hong({body:"2_fuck"});
```

h: *^باشه^.*

`hong({body:"2_you"});`

h: تو.

(...500)

b: چ

(...1500)

`bb({eyes:"wat_2"});`

b: چی؟

`hong({body:"phone1", eyes:"anger", mouth:"anger"});`

h: می‌خوام به اون مهمانی بگم بله،

{{if _.act1g=="go"}}
h: نه برای اینکه تو می‌خوای، بلکه چون *خودم* می‌خوام.
{{/if}}

{{if _.act1g=="dont"}}
h: دقیقاً *چون* تو نمی‌خوای.
{{/if}}

```
hong({body:"putaway"});
sfx("rustle");
```

h: تو کنترلِ من رو در دست نداری.

```
sfx("rustle2");
hong({body:"0_sammich", eyes:"0_annoyed", mouth:"0_neutral"});
```

h: حالا اجازه بده تو آرامشِ ^لعنتی^ این ساندویچِ خوشمزه رو بخورم.

`hong({body:"2_sammich_eat"});`

(...601)

```
sfx("sandwich");
hong({body:"2_sammich_eaten", eyes:"0_lookaway", mouth:"0_chew1"})
```

(...601)

```
bb({body:"normal", eyes:"uncertain", mouth:"shut"});
Game.OVERRIDE_TEXT_SPEED = 0.5;
```

b: ...

```
bb({eyes:"normal_right"});
Game.OVERRIDE_TEXT_SPEED = 1;
```

b: ...

```
bb({eyes:"fear"});
Game.OVERRIDE_TEXT_SPEED = 4;
```

b: ..................

(...500)

`bb({mouth:"normal"});`

[آآآ داریم می‌میریم](#act1h_death) `Game.OVERRIDE_CHOICE_LINE = true;`

[آآآ همه از ما متنفرن](#act1h_loneliness) `Game.OVERRIDE_CHOICE_LINE = true;`

[آآآ ما آدمای افتضاحی هستیم](#act1h_worthless) `Game.OVERRIDE_CHOICE_LINE = true;`

# act1h_death

```
bb({body:"fear"});
Game.OVERRIDE_TEXT_SPEED = 3;
```

b: آآآ داریم می‌میریم آآآآآآآآآآآآ

```
hong({body:"3_defeated1"});
attack("100p", "harm");
```

(...2500)

(#act1i)

# act1h_loneliness

```
bb({body:"fear"});
Game.OVERRIDE_TEXT_SPEED = 3;
```

b: آآآ همه از ما متنفرن آآآآآآآآآآآآ

```
hong({body:"3_defeated1"});
attack("100p", "alone");
```

(...2500)

(#act1i)

# act1h_worthless

```
bb({body:"fear"});
Game.OVERRIDE_TEXT_SPEED = 3;
```

b: آآآ ما آدمای افتضاحی هستیم آآآآآآآآآآآآ

```
hong({body:"3_defeated1"});
attack("100p", "bad");
```

(...2500)

(#act1i)

# act1i

```
bb({mouth:"smile_lock", eyes:"smile", body:"normal"});
music('battle', {volume:0.5});
```

n: تبریک

(...500)

n: با موفقیت از نیازهای فیزیکی + اجتماعی + اخلاقی آدمت محافظت کردی

n: حالا ببین چقدر سپاسگزارن!

(...500)

n: حالا که انرژیشون صفره، می‌تونی مستقیماً رفتارشون رو کنترل کنی

`bb({mouth:"smile", eyes:"normal"});`

n: حرکتِ نهایی‌ت رو انتخاب کن

`bb({mouth:"small_lock", eyes:"fear"});`

n: *کارشون رو تموم کن*

[{جنگ: به گوشیِ استرس‌سازت تنبیه بده!}](#act1i_phone) `Game.OVERRIDE_CHOICE_LINE=true`

[{فرار: مثل توپ جمع شو و گریه کن!}](#act1i_cry) `Game.OVERRIDE_CHOICE_LINE=true`

# act1i_phone

`bb({mouth:"normal", eyes:"narrow"})`

b: گوشیت بهت حمله‌ی هراس داشت می‌داد!

`bb({eyes:"anger"})`

b: زوکربرگ و رفقاش سلامت روانت رو برای پولِ سرمایه‌گذارانِ خطرپذیر می‌رباین!

```
bb({body:"fear", eyes:"fear"});
hong({body:"3_defeated2"});
Game.OVERRIDE_TEXT_SPEED = 1.5;
```

b: گوشیت رو تنبیه کن! نابودش کن! بکشش!

```
Game.OVERRIDE_TEXT_SPEED = 2.5;
bb({body:"flail"});
hong({body:"3_defeated3"});
_.act1_ending = "fight";
```

b: بکشش بکشش بکشش بکشش بکشش بکشش بکشش بکشش بکشش بکشش بکشش بکشش بکشش بکشش بکشش بکشش بکشش بکشش بکشش بکشش بکشش بکشش بک--

(#act1j)

# act1i_cry

`bb({eyes:"fear", mouth:"normal"})`

b: همه‌ی دنیا پر از خطره!

```
bb({body:"fear"});
hong({body:"3_defeated2"});
Game.OVERRIDE_TEXT_SPEED = 1.5;
```

b: مثل زرگشت عمل کن! برای دفاع از خودت مثل توپ جمع شو!

```
Game.OVERRIDE_TEXT_SPEED = 2.5;
bb({body:"flail"});
hong({body:"3_defeated3"});
_.act1_ending = "flight";
```

b: جمع شو و گریه کن جمع شو و گریه کن جمع شو و گریه کن جمع شو و گریه کن جمع شو و گریه کن جمع شو و گریه ک--

(#act1j)

# act1j

`SceneSetup.act1_outro()`
