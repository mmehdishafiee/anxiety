# act4

```
SceneSetup.act4();
publish("SAVE_GAME", ["act4"]);
Game.FORCE_CANT_SKIP = true;
```

(...5001)

```
publish("set_how_many_prompts", [1]);
Game.FORCE_CANT_SKIP = false;
Game.CLICK_TO_ADVANCE = true;
```

n3: (بازی خودش سیو شد)

```
Game.clearText();
Game.FORCE_CANT_SKIP = true;
```

(...1001)

```
var hong_frame = _.INJURED ? 9 : 0;
publish("act4", ["hong_walks_in",hong_frame]);
sfx("grass_step1", {volume:0.1});
```

(...666)

```
publish("act4", ["hong_walks_in", "next"]);
sfx("grass_step2", {volume:0.2});
```

(...666)

```
publish("act4", ["hong_walks_in", "next"]);
sfx("grass_step1", {volume:0.25});
```

(...666)

```
publish("act4", ["hong_walks_in", "next"]);
sfx("grass_step2", {volume:0.3});
```

(...666)

```
publish("act4", ["hong_walks_in", "next"]);
sfx("grass_step1", {volume:0.35});
```

(...1667)

```
publish("act4", ["hong_walks_in", "next"]);
sfx("grass_step2", {volume:0.35});
```

(...666)

```
publish("act4", ["hong_walks_in", "next"]);
sfx("grass_step1", {volume:0.35});
```

(...666)

```
publish("act4", ["hong_walks_in", "next"]);
sfx("grass_step2", {volume:0.35});
```

(...1333)

```
publish("act4", ["hong_walks_in", "next"]);
sfx("grass_step1", {volume:0.20});
```

(...167)

```
publish("act4_hong_sits");
```

(...66)

```
publish("act4", ["hong_transition", "next"]);
sfx("squeak");
```

(...133)

`publish("act4", ["hong_transition", "next"]);`

(...1333)

```
publish("act4", ["hong_transition", "next"]);
sfx("rustle");
```

(...333)

`publish("act4", ["hong_transition", "next"]);`

(...1001)

```
publish("act4", ["hong_transition", "next"]);
```

(...333)

```
publish("act4", ["hong_transition", 9]);
sfx("sandwich");
```

(...333)

`publish("act4", ["hong_transition", 10]);`

(...333)

`publish("act4", ["hong_transition", 9]);`

(...333)

`publish("act4", ["hong_transition", 10]);`

(...333)

`publish("act4", ["hong_transition", 9]);`

(...333)

`publish("act4", ["hong_transition", 10]);`

(...333)

`publish("act4", ["hong_transition", "next"]);`

(...1466)

`publish("act4-out-1");`

(...201)

`publish("act4", ["hong_transition", "next"]);`

(...99)

`publish("act4", ["hong_transition", "next"]);`

(...99)

`publish("act4", ["hong_transition", "next"]);`

(...99)

`publish("act4", ["hong_transition", "next"]);`

(...99)

`publish("act4", ["hong_transition", "next"]);`

(...99)

`publish("act4", ["hong_transition", "next"]);`

(...99)

`publish("act4", ["hong_transition", "next"]);`

(...99)

`publish("act4", ["hong_transition", "next"]);`

(...99)

```
publish("act4-show-chars");
Game.FORCE_CANT_SKIP = false;
```

(...901)

`hong({body:"sigh_1"})`

(...601)

```
hong({body:"sigh_2"});
bb({eyes:"look_down"});
```

h: *آه*

```
hong({body:"hold", eyes:"normal", mouth:"normal"});
bb({eyes:"normal"});
```

h: پس ^لعنتی^ نکته‌ی این داستان چی بود؟

`hong({body:"one_up", eyes:"annoyed"})`

h: اصلاً چی *یاد* گرفتیم؟ من *داشتم* احمقانه عمل می‌کردم، «رفقام» *داشتن* ازم استفاده می‌کردن، و تقریباً ^لعنتی^ *مُردیم*.

`hong({body:"normal", eyes:"normal"})`

{{if _.INJURED}}
[آره، چه برسه به صورت‌حساب بیمارستان.](#act4a_bill)
{{/if}}

{{if !_.INJURED}}
[آره، چه برسه به آسیبِ کبد.](#act4a_liver)
{{/if}}

[آره، اون *واقعاً* بدترین سناریو بود.](#act4a_worst)

[آره، من درست می‌گفتم.](#act4a_right)

# act4a_bill

`hong({eyes:"annoyed_l", mouth:"narrow"});`

h: درسته. فکر نکنم بیمه‌ام «احمق بودن» رو پوشش بده.

`hong({eyes:"annoyed", mouth:"normal"});`

b: و با این حال... زنده موندیم!

`hong({eyes:"normal"});`

h: ؟

(#act4b)

# act4a_liver

`bb({eyes:"normal_d"});`

b: قطعاً چند سالی از امید به زندگیمون کم کردیم...

`bb({eyes:"surprise"});`

b: ولی حداقل هنوز *داریم* امید به زندگی! زنده موندیم!

```
hong({eyes:"surprise"});
bb({eyes:"normal"});
```

h: ؟

(#act4b)

# act4a_worst

`bb({eyes:"normal_d"});`

b: و با این حال...

h: هوم؟

`bb({eyes:"surprise"});`

b: زنده موندیم!

(#act4b)

# act4a_right

`bb({eyes:"normal_d"});`

b: ولی... تو هم درست می‌گفتی.

`hong({eyes:"surprise"});`

h: هوم؟

`bb({eyes:"normal"});`

b: من *همون* گرگ بودم که به گرگ فریاد زد. پس وقتی خطرِ *واقعی* اومد، تو – به درستی – بهم باور نکردی.

`bb({eyes:"surprise_r"});`

b: و با این حال، زنده موندیم!

(#act4b)

# act4b

```
bb({eyes:"normal", mouth:"normal"});
hong({eyes:"normal", mouth:"normal"});
```

b: با وجود همه‌چیز، هنوز اینجاییم.

`hong({eyes:"suspect"});`

{{if _.INJURED}}
h: انقدر آرومی با اینکه تازه یه تجربه‌ی نزدیک به مرگ داشتیم.
{{/if}}

{{if !_.INJURED}}
h: انقدر آرومی با اینکه تازه یه تجربه‌ی *تقریباً* نزدیک به مرگ داشتیم.
{{/if}}

```
hong({eyes:"normal"});
bb({eyes:"annoyed_d", mouth:"narrow"});
```

b: خب، باعث می‌شه بقیه‌ی چیزا نسبتاً کمتر ترسناک بنظر بیان. همچنین باعث شده فکر کنم.

`bb({eyes:"normal", mouth:"normal"});`

b: اگه جنگیدنِ من با تو بده، چون ازت محافظت نمی‌کنه...

h: ولی جنگیدنِ من با تو *هم* بده، چون فقط باعث می‌شه بلندتر فریاد بزنی...

`bb({eyes:"normal_r"})`

b: پس شاید...

`bb({eyes:"normal"})`

h: شاید لازم نیست بجنگیم.

```
Game.FORCE_CANT_SKIP = true;
Game.clearText();
```

(...301)

`publish("smash",[0]);`

(...2001)

```
publish("smash",[1]);
sfx("smash_glass");
```

(...2601)

```
publish("smash",[2]);
bb({eyes:"normal", mouth:"normal"});
hong({eyes:"normal", mouth:"normal"});
```

(...2001)

`Game.FORCE_CANT_SKIP = false;`

(#act4b_2)

# act4b_2

```
music('dontfight',{fade:5, volume:0.6});
bb({eyes:"annoyed_d"});
```

b: من گرگِ بدِ بزرگ نیستم. ولی سگِ نگهبان هم نیستم.

`bb({eyes:"sad_d"})`

b: من یه سگِ پناهگاهِ زده‌شده‌ام.

`bb({eyes:"sad"})`

b: ما چیزای سختی رو گذروندیم. شاید تروما یا بی‌مهری. برای همینه که بعضی وقتا بیش‌ازحد واکنش نشون می‌دم و می‌گم:

```
sfx("yaps", {volume:0.6});
bb({body:"yap_1"});
Game.FORCE_CANT_SKIP = true;
Game.WORDS_HEIGHT_BOTTOM = 215;
Game.FORCE_TEXT_DURATION = 90;
Game.FORCE_NO_VOICE = true;
```

b: واق واق واق واق واق

(...1884)

```
Game.WORDS_HEIGHT_BOTTOM = -1;
Game.FORCE_CANT_SKIP = false;
bb({body:"normal", mouth:"scream", eyes:"scream_sad"});
```

b: ولی من *نمی‌خوام* یه سگِ ترسناک باشم! می‌خوام ازت محافظت کنم! می‌خوام یه سگِ خوب باشم!

`bb({eyes:"sad", mouth:"normal"});`

b: آدم... کمک می‌کنی این گرگ رو رام کنی؟

`hong({eyes:"sad"})`

h: من... سعی می‌کنم.

`hong({eyes:"normal_l", body:"chin", mouth:"narrow"})`

h: باشه. رابطه‌ی سالم با احساسات. رابطه‌ها به ارتباط نیاز دارن. پس بیا ارتباط برقرار کنیم.

`hong({eyes:"normal", body:"hands_1", mouth:"normal"})`

h: پنج دقیقه‌ی بعدی خیلی cheesy به نظر می‌رسه، ولی بیا تا درست بشه تقلبش کنیم.

```
hong({body:"hands_2", mouth:"normal"});
```

h: ای گرگِ درون... *تو* چه حسی داری؟

n2: مجموع ترس‌های استفاده‌شده:

n2: *آسیب‌دیدن* {{_.attack_harm_total}}، *دوست‌نداشته‌شدن* {{_.attack_alone_total}}، *آدم بد بودن* {{_.attack_bad_total}}

n2: اول می‌خوای درباره‌ی کدوم ترس حرف بزنیم؟ (بقیه رو بعداً می‌تونی انجام بدی)

```
_.a4_fears_discussed = 0;
_.num_thanks = 0;
hong({body:"normal"});
bb({eyes:"normal"});
```

[می‌ترسم آسیب ببینیم.](#act4_harm)

[می‌ترسم تنها بمونیم.](#act4_alone)

[می‌ترسم آدمای بدی باشیم.](#act4_bad)

# act4_harm

```
_.a4_talked_about_harm = true;
_.a4_fears_discussed += 1;
```

`bb({eyes:"normal_d"})`

b: می‌خوام از نیازت به امنیتِ فیزیکی محافظت کنم،

`bb({eyes:"sad_d"})`

b: ولی *کل دنیا* انقدر خطرناک به نظر می‌رسه. انقدر پر از تراژدی و شر.

`bb({eyes:"sad"})`

{{if _.a4_fears_discussed==1}}
b: نمی‌دونم، دیگه کافیه *من* انتخاب کنم چی بگم. *تو* چی می‌گی، آدم؟
{{/if}}

{{if _.a4_fears_discussed==2}}
b: بازم، برگرد به تو، آدم. فکر می‌کنی چی؟
{{/if}}

{{if _.a4_fears_discussed==3}}
b: فکر دیگه‌ای داری، آدم؟
{{/if}}

`Game.OVERRIDE_CHOICE_SPEAKER = "h"`

[درست می‌گی. پس بریم از خودمون محافظت کنیم.](#act4_harm_skills)

[بریم خودمون رو به خطرِ *بیشتری* در معرض بذاریم.](#act4_harm_exposure)

[ممنون.](#act4_thanks) `_.thanks_for = "امنیت فیزیکی";`

# act4_harm_skills

`bb({eyes:"look_down", body:"paw"})`

b: ولی... چطور؟ من دندون و چنگ دارم، ولی فقط یه استعارم.

```
bb({ body:"normal", eyes:"normal" });
hong({ body:"one_up", eyes:"surprise" });
```

h: می‌تونیم دفاع شخصی یاد بگیریم؟ به یه اجتماعی که همو محافظت می‌کنن ملحق بشیم؟ سلامت کلی و مرزهای شخصی‌مون رو بهتر کنیم؟

```
bb({ eyes:"annoyed_r" });
hong({ body:"normal", eyes:"normal" });
```

b: شاید، ولی...

[از کجا شروع کنیم اصلاً؟](#act4_harm_skills_start)

[اگه بازم جواب ندن چی؟](#act4_harm_skills_work)

[اگه رو «امنیت» زیاده‌روی کنیم چی؟](#act4_harm_skills_overboard)

# act4_harm_skills_start

`bb({ eyes:"sad_d" })`

b: انقدر کار هست، انقدر چیز باید درباره‌ی خودمون درست کنیم. اصلاً با *چی* شروع کنیم؟

`hong({ body:"shrug", eyes:"surprise" })`

h: داریم همین الان شروع می‌کنیم.

`bb({ eyes:"normal", mouth:"narrow" })`

b: ها؟

```
bb({ body:"normal", mouth:"normal" });
hong({ body:"normal", mouth:"normal", eyes:"normal"});
```

h: داریم همین الان ارتباطِ خوب رو تمرین می‌کنیم. که بهمون کمک می‌کنه خطر رو بهتر تشخیص بدیم، با خطاهای کمتر،

`hong({ eyes:"surprise" });`

h: و *اون* بهمون کمک می‌کنه از آسیب محافظت کنیم!

`hong({ eyes:"normal", mouth:"normal" });`

h: پس: این *همون* تمرین دفاع شخصیه.

`bb({ eyes:"normal_r" })`

b: هوم. انتظار بیشتر این رو داشتم:

```
Game.FORCE_CANT_SKIP = true;
Game.clearText();
hong({ eyes:"sad", mouth:"smile" });
bb({ body:"karate_1" });
sfx("hiya");
```

(...1001)

`Game.FORCE_CANT_SKIP = false;`

(#act4_something_else)

# act4_harm_skills_work

`bb({ eyes:"normal" });`

h: درسته، هیچ راهی نیست که ۱۰۰٪ از خودمون محافظت کنیم...

`hong({ body:"one_up" });`

h: ولی حتی ۱٪ بهتر شدن هم ارزشی داره، نه؟

```
bb({ eyes:"annoyed" });
hong({ normal:"one_up" });
```

b: داری لیوان رو نه ۹۹٪ خالی، بلکه ۱٪ پر می‌بینی؟

`bb({ eyes:"normal" });`

h: که اگه تو صحرا سرگردون باشی هنوز ارزشی داره.

`bb({ eyes:"closed" });`

b: خب. پس به سلامتی.

(#act4_something_else)

# act4_harm_skills_overboard

`bb({ body:"chest", eyes:"annoyed" })`

b: یعنی، تنها دلیلی که هشدارهای من رو نادیده گرفتی این بود که *من* رو امنیت زیاده‌روی کردم! 

`bb({ body:"normal", eyes:"normal" })`

h: نه، درست می‌گی. می‌خوایم امنیت رو در حد اعتدال انجام بدیم. همه‌چیز در حد اعتدال.

`bb({ eyes:"suspect" })`

b: ببخشید، *همه‌چیز* در حد اعتدال؟

`hong({ eyes:"annoyed" })`

h: *تعدادِ متعادلی از چیزا* در حد اعتدال.

```
bb({ eyes:"closed" });
hong({ eyes:"normal" });
```

b: ممنون که جمله‌هات رو بازگشتی سازگار کردی.

(#act4_something_else)


# act4_harm_exposure

`bb({ mouth:"scream_talk", eyes:"scream", MOUTH_LOCK:true });`

b: *چی*

```
bb({ mouth:"narrow", eyes:"suspect" });
hong({ body:"one_up" });
```

h: یعنی، بذار بگم یه سگی از رعدوبرق می‌ترسه.

`hong({ body:"hands_1" });`

h: یه ترفندی که مربی‌ها استفاده می‌کنن اینه که ضبط‌شده‌ی رعدوبرق رو با صدای کم پخش کنن، بعد به سگ جایزه بدن که آروم بمونه.

`hong({ body:"hands_2" });`

h: طی چند روز، مربی صدا رو کم‌کم بلندتر می‌کنه، تا سگ ترسش از رعدوبرق رو غلبه کنه.

```
hong({ body:"normal", eyes:"surprise" });
bb({ mouth:"normal", eyes:"normal" });
```

h: بهش می‌گن درمانِ مواجهه‌ای!

`hong({ body:"point", eyes:"normal" });`

h: چون تو یه سگی، باید روی تو هم کار کنه، نه؟ همه‌ی پستاندارها همون واکنش جنگ یا گریز رو دارن.

`hong({ body:"normal" });`

[اگه *زیادی* بی‌حس بشیم چی؟](#act4_harm_exposure_overboard)

[اگه به خطرِ *واقعی* در معرض باشیم چی؟](#act4_harm_exposure_hurt)

[من گرگم، نه سگ.](#act4_harm_exposure_dog) `bb({ eyes:"suspect" })`

# act4_harm_exposure_dog

h: و بهت مهربونی و صبر نشون می‌دم تا تبدیل بشی به یه توله‌سگِ کوچولوی خانگی.

`bb({ MOUTH_LOCK:true })`

b: ...

`bb({ eyes:"sad", mouth:"smile" })`

b: آآآو.

(#act4_something_else)

# act4_harm_exposure_overboard

`bb({ eyes:"annoyed" })`

b: ما *تازه* دیدیم چی می‌شه اگه ترست رو خاموش کنی – خودت رو تو موقعیت‌های *واقعاً* خطرناک می‌ذاری.

`bb({ eyes:"angry_r", body:"one_up" })`

b: ضمناً، *زیادی* بی‌حس شدن ما رو به روان‌پریش تبدیل نمی‌کنه؟

`bb({ mouth:"scream", eyes:"scream", body:"two_up" })`

b: به زودی داریم به خودمون جایزه می‌دیم در حالی که داریم پورنِ قتل تماشا می‌کنیم!

`hong({ eyes:"annoyed" })`

h: من... فکر کنم یه خطی بین اون و رعدوبرق هست.

`bb({ body:"normal", mouth:"normal", eyes:"suspect" })`

b: ولی دقیقاً *کجا*، آدم؟ *کجا؟!*

`hong({ eyes:"surprise", body:"one_up" })`

h: نمی‌دونم. ولی *تو* می‌تونی بهم کمک کنی!

`hong({ eyes:"normal", body:"normal" })`

h: با کار و چانه‌زنی با تو، اون خط رو می‌کشیم.

`bb({ body:"paw", mouth:"narrow", eyes:"closed" })`

b: باشه. ولی من انگشتِ شست ندارم، پس تو باید رسمش کنی.

(#act4_something_else)

# act4_harm_exposure_hurt

`bb({ body:"two_up", eyes:"angry_r" })`

{{if _.INJURED}}
b: مثلاً: ما از یه *پشت‌بامِ* لعنتی پریدیم!
{{/if}}

{{if !_.INJURED}}
b: مثلاً: ما تقریباً از یه *پشت‌بامِ* لعنتی پریدیم!
{{/if}}

```
hong({ eyes:"annoyed" });
bb({ body:"normal", eyes:"annoyed" });
```

h: نه درست می‌گی. یه نفر *می‌تونه* زیادی دور بزنه.

`hong({ eyes:"normal" });`

h: ولی برای همینه که اگه درمانِ مواجهه‌ای بکنیم، کوچیک شروع می‌کنیم و قدم‌های کوچیک بالا می‌ریم.

h: درست قبل از اینکه به خطرِ *واقعی* برسیم، می‌ایستیم.

`bb({ eyes:"annoyed_r", mouth:"narrow" });`

b: آره من خط رو بین شنیدن رعدوبرقِ بلند و ایستادن تو طوفان با یه کلاه بلند تیز می‌کشم.

(#act4_something_else)

# act4_thanks

`_.num_thanks += 1`

{{if _.num_thanks==1}}
(#act4_thanks_1)
{{/if}}

{{if _.num_thanks==2}}
(#act4_thanks_2)
{{/if}}

{{if _.num_thanks==3}}
(#act4_thanks_3)
{{/if}}

# act4_thanks_1

`bb({ MOUTH_LOCK:true })`

b: ...

`bb({ eyes:"annoyed" })`

b: صبر کن، هیچ بحثی موافق یا مخالف با چیزی که احساس می‌کنم نیست؟ فقط... «ممنون»؟

`hong({ eyes:"surprise", body:"shrug" })`

h: آره! ممنون که نگرانیت رو برای {{_.thanks_for}} من نشون دادی.

```
bb({ eyes:"closed_annoyed", MOUTH_LOCK:true });
hong({ eyes:"normal", body:"normal" });
```

b: ...

h: خوبی؟

`bb({ eyes:"super_sad", mouth:"narrow" });`

b: قبلن هیچ‌وقت بهم *ممنون* نگفتی.

`hong({ mouth:"smile" });`

h: آآآو تو گرگِ هراسِ خزدارِ بزرگ.

(#act4_something_else)

# act4_thanks_2

h: حتی اگه زیاده‌روی می‌کنی، قدردانِ اینم که مراقب {{_.thanks_for}} منی.

`bb({ eyes:"annoyed" })`

b: صبر کن... داری فقط «ممنون» تکرار می‌کنی که از حرف زدن درباره‌ی این ترس‌ها فرار کنی، نه؟

```
bb({ eyes:"normal" });
hong({ eyes:"annoyed", body:"chin" });
```

h: خب، چیزا پیچیده‌ان، و همیشه جواب آماده ندارم.

`hong({ eyes:"annoyed_l", body:"one_up" })`

h: این‌طوری نیست که زندگی بهت یه لیست ۳تایی از جواب‌های دیالوگِ آماده بده.

`hong({ eyes:"normal", mouth:"smile", body:"normal" })`

h: ولی فعلاً، حداقل می‌تونم تشکر کنم.

b: خب، منم ممنون، که با صبر بهم گوش دادی.

`bb({ eyes:"closed" });`

b: تو پستاندارِ گوشتِ بی‌موِ کوچیک.

(#act4_something_else)

# act4_thanks_3

h: حتی اگه پارس‌هات منو می‌ترسونن، فقط داری تلاش می‌کنی {{_.thanks_for}} من رو محافظت کنی.

`bb({ eyes:"smile_r" });`

b: باشه، اگه این‌جوری بهم بگوشی، اینترنت یه ایده‌های عجیبی درباره‌ی ما می‌گیره.

```
bb({ eyes:"smile" });
hong({ eyes:"annoyed" });
```

h: بیا ببینم، من فقط یه بچه‌ی دانشجو-سنِ آسیب‌پذیرم و تو یه گرگِ بزرگ ترسناک. بدترین اتفاقی که می‌تونه بیفته چ--

`hong({ eyes:"normal", body:"point" });`

h: در واقع، به اون جواب نده.

(#act4_something_else)




# act4_alone

```
_.a4_talked_about_alone = true;
_.a4_fears_discussed += 1;
```

`bb({ eyes:"sad_d" });`

b: می‌خوام مطمئن بشم که اون نیازِ عمیقِ انسانی به تعلق رو برآورده می‌کنی...

`bb({ eyes:"sad_u" });`

b: ولی نگرانم که اگه کسی مارو بشناسه – *واقعی* مارو – همه رو فراری بدیم.

`bb({ eyes:"sad" });`

{{if _.a4_fears_discussed==1}}
b: نمی‌دونم، دیگه کافیه *من* انتخاب کنم چی بگم. *تو* چی می‌گی، آدم؟
{{/if}}

{{if _.a4_fears_discussed==2}}
b: بازم، برگرد به تو، آدم. فکر می‌کنی چی؟
{{/if}}

{{if _.a4_fears_discussed==3}}
b: فکر دیگه‌ای داری، آدم؟
{{/if}}

`Game.OVERRIDE_CHOICE_SPEAKER = "h"`

[موافقم: بریم روی زندگی اجتماعیمون کار کنیم.](#act4_alone_skills)

[فکر کنم آدم‌ها مارو دوست دارن. بریم بفهمیم؟](#act4_alone_experiment)

[ممنون.](#act4_thanks) `_.thanks_for = "تعلق اجتماعی";`

# act4_alone_skills

```
bb({ eyes:"normal" });
hong({ body:"chin" });
```

h: می‌تونیم مهارت‌هایی مثل سوال پرسیدن، گوش دادن و همدلی، باز و آسیب‌پذیر بودن و اینا رو تمرین کنیم؟

`hong({ eyes:"normal_l" });`

h: یا عادت‌های اجتماعیِ بهتری بسازیم، مثل زمان‌بندیِ وقت با رفقا یا رفتن منظم به جمع‌ها؟

`hong({ body:"one_up" });`

h: یا می‌تونیم یاد بگیریم که با رد شدن راحت‌تر باشیم.

`hong({ eyes:"normal" });`

h: یا یاد بگیریم بفهمیم که آدم‌ها *ندارن* مارو رد می‌کنن، فقط خستن یا چهره‌ی استراحتِ خشنه دارن.

```
hong({ body:"normal" });
bb({ eyes:"annoyed_r" });
```

b: خیلی گزینه هست. ولی، درباره‌ی «یادگیری مهارت‌های اجتماعی»...

[این *دستکاری* نیست؟](#act4_alone_skills_manipulative)

[این مارو *راحت‌تر دستکاری‌شونده* نمی‌کنه؟](#act4_alone_skills_manipulated)

[اگه بازم شکست بخوریم چی؟](#act4_alone_skills_fail)

# act4_alone_skills_manipulative

`bb({ eyes:"suspect" });`

b: آخه قاتل‌های سریالی که می‌تونن احساسات قربونیاشون رو بخونن در «همدلی» عالین؟

`bb({ eyes:"annoyed" });`

b: چارلز منسون رفیق جمع نکرد و رو آدما نفوذ نکرد؟

`hong({ eyes:"annoyed", body:"chin" });`

h: نه، درست می‌گی.

h: «مهارت‌های اجتماعی» هیچ معنایی نداره اگه واقعاً *به* آدما اهمیت ندیم.

`hong({ body:"normal" });`

h: اساساً، فقط ^کیر^ نباش.

`bb({ eyes:"annoyed", mouth:"smile" });`

b: این دقیقاً یه کپشنِ پوسترِ انگیزشیه.

`hong({ body:"shrug", mouth:"narrow" });`

h: «^کیر^ نباش™»

(#act4_something_else)

# act4_alone_skills_manipulated

`bb({ eyes:"angry" })`

b: تبدیل به یه زیرپاییِ خوش‌آمد می‌شیم که می‌گه خواهش و تشکر در حالی که آدما پاهاشون رو رومون پاک می‌کنن!

`bb({ mouth:"scream", eyes:"scream" })`

b: انقدر کون می‌لیسیم که انگار رژِ لبِ قهوه‌ای زدیم!

```
bb({ mouth:"normal", eyes:"normal" });
hong( body:"chin" });
```

h: نه، درست می‌گی. «مهارت‌های اجتماعی» نمی‌تونه فقط درباره‌ی خوشحال کردنِ بقیه باشه، باید درباره‌ی گذاشتن *مرز* هم باشه.

`hong( body:"one_up" });`

h: نمی‌تونیم بقیه رو به خونمون دعوت کنیم، اگه دیواری نداشته باشیم که خونمون رو نگه داره.

```
hong( eyes:"angry", mouth:"narrow" });
bb( eyes:"annoyed", mouth:"smile" });
```

h: ضمناً... در مورد اون تصویرِ ذهنیِ رژ لب... *اه؟؟*

(#act4_something_else)

# act4_alone_skills_fail

`bb({ eyes:"annoyed" });`

h: ممکنه شکست بخوریم. در واقع، *حتماً* شکست می‌خوریم.

```
bb({ eyes:"normal" });
hong({ eyes:"surprise", body:"shrug" });
```

h: و اشکالی نداره! شکست خوردن روشیه که هر کسی اولِ کار یاد می‌گیره!

`hong({ body:"normal", eyes:"normal" });`

h: پس بریم با هم به جلو شکست بخوریم، آره؟

`bb({ eyes:"normal_r" });`

b: آره، حدس می‌زنم... بدترین حالت، می‌تونیم شهر رو ترک کنیم و یه هویت جدید بگیریم.

`bb({ eyes:"normal" });`

h: آره فکر کنم امروزه فقط دو تا بیت‌کوین هزینه داره.

(#act4_something_else)

# act4_alone_experiment

```
hong({ body:"one_up" });
bb({ eyes:"normal" });
```

h: می‌تونیم چند تا آزمایش بکنیم!

`hong({ body:"chin" });`

h: می‌تونیم به یه رفیق پینگ بدیم که بیرون بریم، با یه رفیق قدیمی رابطه رو تازه کنیم، یا حتی فقط با باریستا حرف بزنیم.

`hong({ body:"normal" });`

h: فکر کنم می‌فهمیم که بیشتر از چیزی که فکر می‌کنیم دوست‌داشتنی هستیم.

`bb({ eyes:"annoyed" });`

[اگه اینا بردهای کوچیک و ارزون باشن چی؟](#act4_alone_experiment_cheap)

[اگه این یه بارِ روی دوش بقیه باشه چی؟](#act4_alone_experiment_burden)

[ولی حرفِ کوچیک *واقعی* ما نیست!](#act4_alone_experiment_real_us)

# act4_alone_experiment_real_us

`bb({ eyes:"sad" });`

b: اگه یه لبخندِ سطحی بزنیم، هیچ‌وقت واقعاً به کسی وصل نمی‌شیم،

`bb({ eyes:"super_sad" });`

b: *ولی* اگه باز بشیم، بقیه همه‌ی درونِ خراب‌مون رو می‌بینن!

`hong({body:"chin", mouth:"narrow", MOUTH_LOCK:true})`

h: ...

```
hong({body:"normal", mouth:"normal"});
bb({eyes:"normal"});
```

h: غلت بزن.

b: چی.

`hong({body:"hands_1"})`

h: وقتی سگ‌ها می‌خوان عشق و اعتماد نشون بدن، با نشون دادنِ شکمشون خودشون رو آسیب‌پذیر می‌کنن.

`hong({body:"one_up"})`

h: شاید ما هنوز اون‌قدر امن نباشیم که زیادی آسیب‌پذیر بشیم، ولی با تمرین کافی،

`hong({body:"normal", eyes:"surprise"})`

h: یه روز می‌تونیم نسخه‌ی واقعی‌مون رو به آدم‌ها نشون بدیم – همه‌ی خرابی، همه‌ی انسانیت.

```
hong({eyes:"normal"});
bb({ eyes:"super_sad", mouth:"smile", body:"chest" });
```

b: اگه بهم جایزه بدی غلت می‌زنم.

`bb({ eyes:"normal", mouth:"normal" });`

h: نه.

(#act4_something_else)


# act4_alone_experiment_cheap

b: گفتن «سلام» به باریستا دقیقاً عملکردِ مدال طلا تو المپیکِ پروانه‌ی اجتماعی نیست.

```
hong({ body:"point", eyes:"surprise" });
bb({ eyes:"normal" });
```

h: برای *ما* هست!

`hong({ body:"one_up", eyes:"annoyed" });`

h: تو عرصه‌ی اجتماعی، ما حتی در سبکِ پَر هم نیستیم، ما مثل... سبکِ کوارک هستیم.

`hong({ body:"normal", eyes:"normal" });`

h: اگه مجبوریم با بردهای کوچیک و ارزون شروع کنیم، همینه. باید پله‌ی ۱ رو بریم قبل از پله‌ی ۱۰۰۰.

b: آره! شاید بعد از گفتن «سلام»، بتونیم به گفتن... ارتقا پیدا کنیم...

`bb({ body:"two_up", mouth:"smile", eyes:"smile_u" });`

b: *"چطوری؟"*

`hong({ body:"shrug", mouth:"smile", eyes:"surprise_l" });`

h: *"خیلی!"*

(#act4_something_else)

# act4_alone_experiment_burden

`bb({ eyes:"suspect_r" })`

b: شاید باریستا فقط می‌خواد یه قهوه بسازه، نه اینکه *آزمایشی* باشه که بفهمیم مهارت‌های اجتماعیمون گه هستن یا نه.

`bb({ eyes:"annoyed" })`

h: خب، اگه معلوم بشه ما *واقعاً* بار روی دوشیم...

```
hong({ eyes:"surprise" });
bb({ eyes:"normal" });
```

h: اینم خوبه که بدونیم!

`hong({ eyes:"normal" });`

h: اون‌وقت می‌تونیم یاد بگیریم چطور فعالانه از آدم‌ها بپرسیم با چی راحتن، تا مرزهای بقیه رو بفهمیم و احترام بذاریم.

```
hong({ eyes:"annoyed_l", mouth:"narrow" });
bb({ eyes:"annoyed", mouth:"smile" });
```

h: می‌دونی، همه‌ی اون ^crap^ـی که تو بروشورهای مشاوره می‌بینی به اسم «مهارت‌های بین فردی».

(#act4_something_else)



# act4_bad

```
_.a4_talked_about_bad = true;
_.a4_fears_discussed += 1;
```

`bb({ eyes:"annoyed_r" })`

b: می‌خوام از نیازهای اخلاقیت دفاع کنم، اون انگیزه‌ای که بشی آدمِ بهتری،

`bb({ eyes:"sad_d" })`

b: ولی فقط حس می‌کنم تو عمق وجود، ما خیلی اساسی... خرابیم.

`bb({ body:"two_up", eyes:"angry" })`

{{if _.INJURED}}
b: و بهم نگو ما خراب *نیستیم*. ما از یه *پشت‌بام* پریدیم.
{{/if}}

{{if !_.INJURED}}
b: و بهم نگو ما خراب *نیستیم*. ما تقریباً از یه *پشت‌بام* پریدیم.
{{/if}}

`bb({ body:"normal", eyes:"sad" })`

{{if _.a4_fears_discussed==1}}
b: نمی‌دونم، دیگه کافیه *من* انتخاب کنم چی بگم. *تو* چی می‌گی، آدم؟
{{/if}}

{{if _.a4_fears_discussed==2}}
b: بازم، برگرد به تو، آدم. فکر می‌کنی چی؟
{{/if}}

{{if _.a4_fears_discussed==3}}
b: فکر دیگه‌ای داری، آدم؟
{{/if}}

`Game.OVERRIDE_CHOICE_SPEAKER = "h"`

[پس خرابیم. بریم خودمون رو درست کنیم.](#act4_bad_fix)

[پس خرابیم. بریم قبولش کنیم.](#act4_bad_accept)

[ممنون.](#act4_thanks) `_.thanks_for = "سلامت اخلاقی";`

# act4_bad_fix

```
bb({eyes:"normal"});
hong({body:"chin"});
```

h: می‌تونیم کم‌کم عادت‌های بهتری بسازیم، زندگیمون رو بیشتر با چیزی که ارزش می‌دیم هم‌راستا کنیم،

`hong({body:"one_up"});`

h: و اگه لازم شد، می‌تونیم کمک حرفه‌ای بگیریم – یه تراپیست یا مشاور.

`hong({body:"normal"});`

h: راه‌هایی هست که خودمون رو درست کنیم.

[اگه نتونیم همه‌ش رو درست کنیم چی؟](#act4_bad_fix_cant)

[اگه *زیادی* درستش کنیم چی؟](#act4_bad_fix_too_much)

[پولِ کمکِ حرفه‌ای رو نداریم.](#act4_bad_fix_afford)

# act4_bad_fix_cant

`hong({eyes:"annoyed"});`

h: نه، حدس می‌زنم درست می‌گی.

h: نمی‌تونیم همه‌ش رو درست کنیم.

`bb({mouth:"scream", eyes:"scream_sad"});`

b: آآآ می‌دونستم همیشه خراب می‌مونیم!

`hong({eyes:"surprise"});`

h: ولی حداقل می‌تونیم *کمتر* خراب باشیم.

```
bb({mouth:"normal", eyes:"annoyed"});
hong({eyes:"sad", mouth:"smile"});
```

h: اسکارها با زمان بهبود پیدا می‌کنن، ولی هیچ‌وقت نمی‌رن. و اشکالی نداره.

`bb({eyes:"annoyed_r"});`

b: حدس می‌زنم. ضمناً،

```
Game.FORCE_TEXT_Y = 460;
Game.clearText();
publish("act4-sexy", [true]);
```

b: اسکارها *سکسین.*

```
Game.FORCE_TEXT_Y = -1;
Game.clearText();
publish("act4-sexy", [false]);
bb({body:"chest", mouth:"smile_talk", MOUTH_LOCK:true, eyes:"sexy"}, 0);
hong({eyes:"normal", mouth:"normal"}, 0);
```

h: لطفاً این کار رو نکن.

(#act4_something_else)

# act4_bad_fix_too_much

`bb({ eyes:"angry_d" })`

b: حال بهم می‌خوره که بگم، ولی... یه بخشی از من *می‌خواد* این اختلال رو داشته باشه.

`bb({ eyes:"angry" })`

b: یعنی، بدون اون، ما *خسته‌کننده* نمی‌شیم؟

`bb({ eyes:"sad_r", body:"one_up" })`

b: بدون اختلال، هنرمون کهنه و بی‌مزه نمی‌شه؟

`bb({ eyes:"sad_u", body:"two_up" })`

b: بدون اختلال، دیگه نمی‌تونیم با رفقامون که اونا هم اختلال دارن ارتباط بگیریم؟

`bb({ eyes:"sad", body:"chest" })`

b: اگه هیچ‌وقت از زندگی راضی بشیم، دیگه خودمون رو برای انجام کارهای بزرگ مجبور نمی‌کنیم؟

`hong({ MOUTH_LOCK:true })`

h: ...

h: اگه حتی بترسیم که... «ترس‌هامون تموم بشن»...

h: فکر نکنم ترس‌هامون تموم بشن.

`bb({ eyes:"smile_u", body:"normal", mouth:"smile" })`

b: اوه، آره! اوف! چه راحتی!

(#act4_something_else)

# act4_bad_fix_afford

`bb({ body:"one_up", eyes:"sexy", mouth:"normal" })`

b: «دکتر، اضطراب دارم که ساعتی ۱۰۰ دلار دارم می‌دم فقط بشنوم بپرسی *این چه حسی بهت می‌ده؟*»

`bb({ body:"paw", eyes:"closed", mouth:"narrow" })`

b: «هوم. و این چه حسی بهت می‌ده؟»

```
bb({ body:"normal", eyes:"normal", mouth:"normal" });
hong({ eyes:"sad" });
```

h: نه، اون یه نگرانیِ کاملاً منطقیه.

`hong({ eyes:"annoyed", mouth:"sad" });`

h: و واقعاً گهه که مراقبتِ بهداشت روان برای خیلی‌ها مقرون‌به‌صرفه نیست.

`hong({ eyes:"normal", mouth:"normal" });`

h: با این حال، چند تا گزینه‌ی ارزون یا رایگان هست:

`hong({ body:"chin" })`

h: گروه‌های حمایت، تراپی آنلاین، مراکز بهداشتی دانشجویی/غیرانتفاعی...

`hong({ body:"hands_1" })`

h: ساختنِ عادت‌هایی مثل مدیتیشن، خوابِ خوب، حرف زدن منظم با رفقا، یادگیری چیزای جدید...

`hong({ body:"hands_2" })`

h: رفتن به کتابخونه برای قرض گرفتن workbookهای روان‌درمانیِ مبتنی بر شواهد...

`hong({ body:"one_up" })`

h: یه لیست کامل از منابع تهِ این بازی هست!

```
hong({ body:"normal" });
bb({ eyes:"annoyed", mouth:"narrow" });
```

b: خب *اون* دیوار چهارم زیاد دوام نیومد.

`hong({ body:"point" });`

h: بعضی چیزا مهم‌تر از قراردادِ روایتن. مثل سلامت روان.

(#act4_something_else)


# act4_bad_accept

```
bb({ eyes:"normal" });
hong({ eyes:"normal_l", body:"one_up", mouth:"narrow" });
```

h: یعنی، این همونیه که تراپیست‌ها می‌گن نه؟ همه‌ی احساساتت رو بپذیر، حتی منفی‌ها رو؟

```
bb({ eyes:"annoyed" });
hong({ eyes:"normal", body:"normal", mouth:"normal" });
```

b: صبر کن.

[«پذیرفتن» به معنای *تسلیم شدن*؟](#act4_bad_accept_give_up)

[«پذیرفتن» به معنای *تأیید کردن*؟](#act4_bad_accept_approve)

[«پذیرفتن» به معنای *تحت‌اللفظی گرفتن*؟](#act4_bad_accept_literally)

# act4_bad_accept_give_up

`bb({ eyes:"angry", body:"one_up" });`

b: فکر می‌کنی مارتین لوتر کینگ می‌گفت، «اوه ما نمی‌تونیم جلو اتوبوس بشینیم، بریم *بپذیریمش*»؟

`bb({ eyes:"angry_r", body:"two_up" });`

b: چرا مجتمعِ صنعتیِ self-help فکر می‌کنه پرچم سفید تکون دادن یه حکمتِ *عمیقه*؟

`bb({ eyes:"annoyed", body:"normal" });`

h: فکر کنم تراپیست‌ها منظورشون از «پذیرفتن» چیزای بده اینه: اذعان به اینکه وجود دارن و سخت‌تغییرن،

h: ولی نه لزوماً تسلیم شدنِ تعهد به تغییر.

`bb({ eyes:"suspect" });`

b: پس تراپیست‌ها باید بگن *اذعان*، نه *پذیرش*.

`hong({ body:"chin", eyes:"annoyed" });`

h: آره حالا که فکرش می‌کنم، «پذیرش» یه کم گیج‌کننده‌ست.

`bb({ eyes:"closed", mouth:"narrow" });`

b: خب، من *اذعان* می‌کنم به اون.

(#act4_something_else)

# act4_bad_accept_approve

`bb({ eyes:"angry" });`

b: مثلاً اینکه *خوبه* که ما خرابیم؟ نه!

`bb({ eyes:"angry_r", body:"one_up" });`

b: همه‌ی اون نویسنده‌های لعنتی هالیوودی که بیماری روانی رو رمانتیک می‌کنن پر از گهن!

`bb({ eyes:"angry", body:"two_up" });`

b: داشتنِ اختلال روانی *گَهه!* زندگی آدما رو می‌دزده! چرا باید اونو «بپذیریم»؟!

`bb({ body:"normal" });`

h: فکر کنم تراپیست‌ها منظورشون از «پذیرفتن» احساساتمون اینه: باهاشون صبور باشیم.

```
hong({ body:"one_up" });
bb({ eyes:"normal" });
```

h: مثل اینکه مبارزه تو شن‌های نرم باعث می‌شه سریع‌تر فرو بری، و راه‌حل اینه که صبورانه صاف بخوابی،

`hong({ eyes:"surprise" });`

{{if _.INJURED}}
h: جنگیدن با تو، ترسم، منو به پریدن از پشت‌بام رسوند.
{{/if}}

{{if !_.INJURED}}
h: جنگیدن با تو، ترسم، تقریباً منو به پریدن از پشت‌بام رسوند.
{{/if}}

`hong({ body:"normal", eyes:"normal" });`

h: در عوض، راه‌حل اینه که کاری که الان داریم می‌کنیم رو بکنیم – نه جنگیدن، بلکه صبورانه کنار هم بودن.

`bb({ eyes:"annoyed" });`

b: پس اونا باید *اون* رو بگن به جای یه کلمه‌ی مشکل‌ساز مثل «پذیرش».

`hong({ body:"chin", eyes:"annoyed" });`

h: آره حالا که فکرش می‌کنم، «پذیرش» یه جورایی گهه.

`bb({ eyes:"closed_annoyed", mouth:"narrow" });`

b: من «پذیرش» رو نمی‌پذیرم.

(#act4_something_else)

# act4_bad_accept_literally

`bb({ eyes:"sad", body:"one_up" });`

b: ولی ما از قبل *می‌دونیم* که نباید منو تحت‌اللفظی بگیری!

`bb({ eyes:"sad_u", body:"two_up" });`

b: کل *مشکل* اینه که می‌خوام بهت کمک کنم، ولی تو استفاده از کلمات برای این کار خیلی گهم!

`bb({ eyes:"sad", body:"normal" });`

h: فکر کنم تراپیست‌ها منظورشون از «پذیرفتن» احساساتت اینه: «باهاشون نجنگ یا نادیده‌شون نگیر.»

`hong({ eyes:"surprise", body:"one_up" });`

h: که بهت گوش بدی، *باهات* کار کنی، ولی حرفت رو نگیری صددرصد حقیقتِ تحت‌اللفظی.

```
hong({ eyes:"normal", body:"normal" });
bb({ eyes:"annoyed", mouth:"normal" });
```

b: پس تراپیست‌ها باید *اون* رو بگن به جای یه کلمه‌ی مبهم و گیج‌کننده مثل «پذیرش».

`hong({ body:"chin", eyes:"annoyed" });`

h: حدس می‌زنم اونا هم تو استفاده از کلمات گهن.

(#act4_something_else)




# act4_something_else

```
bb({ body:"normal", mouth:"normal", eyes:"normal" });
hong({ body:"normal", mouth:"normal", eyes:"normal" });
```

{{if _.a4_fears_discussed==1}}
h: به هر حال، چیز دیگه‌ای هست که بخوای درباره‌ش حرف بزنیم؟
{{/if}}

{{if _.a4_fears_discussed==2}}
h: پس، چیز دیگه‌ای روی دلِ سنگینت هست؟
{{/if}}

{{if _.a4_fears_discussed==3}}
(#act4_something_else_2)
{{/if}}

{{if _.a4_talked_about_harm!=true}}
[می‌ترسم آسیب ببینیم.](#act4_harm)
{{/if}}

{{if _.a4_talked_about_alone!=true}}
[می‌ترسم تنها بمونیم.](#act4_alone)
{{/if}}

{{if _.a4_talked_about_bad!=true}}
[می‌ترسم آدمای بدی باشیم.](#act4_bad)
{{/if}}

[نه، فعلاً خوبم.](#act4c_prelude)

# act4_something_else_2

h: باشه، فکر کنم درباره‌ی همه‌ی ترس‌هامون حرف زدیم.

b: آره، فقط سه تا ترس هست.

h: آره، دقیقاً سه تا.

b: چه راحت.

(#act4c)

# act4c_prelude

h: حرفِ خوبی بود، تیم.

(#act4c)

# act4c

```
Game.clearText();
music(null,{fade:3});
bb({body:"normal", eyes:"normal", mouth:"normal", MOUTH_LOCK:true},0);
hong({body:"normal", eyes:"normal", mouth:"normal"},0);
```

b: ...

`hong({MOUTH_LOCK:true},0)`

h: ...

`bb({eyes:"annoyed_d"})`

b: می‌دونی، این یه *بازی* نیست.

`bb({eyes:"angry_d", body:"one_up"})`

b: ساختن یه رابطه‌ی سالم با احساساتت به اندازه‌ی کلیک کردن روی دکمه‌های یه صفحه ساده نیست.

`bb({eyes:"sad", body:"normal"})`

b: *می‌تونیم* واقعاً کنار بیایم؟

b: *می‌تونیم* با هم، به‌عنوان یه تیم، کار کنیم؟

`hong({eyes:"sad", body:"one_up"})`

h: خب،

```
hong({eyes:"surprise_l"});
bb({eyes:"normal"});
```

a: ب-ب-ببخشید...

```
Game.clearText();
publish("act4-in-2");
music('campus', {volume:0.5, fade:1});
```

(...2101)

(#act4d)

# act4d

`Game.WORDS_HEIGHT_BOTTOM = 221;`

`publish("act4", ["alshire", 0]);`

a: م-مم-ممکنه ناراحت بشی اگه براتون ناهار بشینم؟

`publish("act4", ["alshire", 1]);`

{{if _.TOP_FEAR=="harm"}}
s: *این* کراشته؟ چرا مثل یه قاتلِ روانی تنها می‌شینن؟
{{/if}}

{{if _.TOP_FEAR=="alone"}}
s: از کراشت می‌پرسی می‌تونی بشینی باهاشون؟ می‌دونی چقدر *نیازمند* به نظر می‌رسیم؟!
{{/if}}

{{if _.TOP_FEAR=="bad"}}
s: *این* کراشته؟ ما آرامش و سکوتشون رو قطع کردیم! ما یه باریم!
{{/if}}

`publish("act4", ["alshire", 2]);`

a: م- یعنی- اشکالی نداره اگه نه، من فقط...

`publish("act4", ["alshire", 3]);`

`Game.OVERRIDE_CHOICE_SPEAKER = "h2"`

[صبر کن، تو رو تو مهمانی ندیدم؟](#act4d_recognition) `publish("act4", ["hong_to_alshire",1])`

[آره، حتماً! بیا اینجا.](#act4d_yes) `publish("act4", ["hong_to_alshire",2])`

[ببخشید، الان نیاز به تنهایی دارم.](#act4d_no) `publish("act4", ["hong_to_alshire",8])`

# act4d_recognition

`publish("act4", ["hong_to_alshire",2]);`

h2: آره تو روی مبل بودی! تو اولین مهمانی که رفتم...

`publish("act4", ["hong_to_alshire",10]);`

{{if _.a2_ending=="fight"}}
h2: جایی که اون حمله‌ی هراس رو داشتم و به میزبان مشت زدم.
{{/if}}

{{if _.a2_ending=="flight"}}
h2: جایی که اون حمله‌ی هراس رو داشتم و گریه کردم و در رفتم.
{{/if}}

```
publish("act4", ["hong_to_alshire", 0]);
publish("act4", ["bb_to_alshire", _.INJURED ? 3 : 1]);
```

b: صبر کن آدم، ممکنه داریم ناراحتشون می‌کنیم.

```
publish("act4", ["hong_to_alshire", 3]);
publish("act4", ["bb_to_alshire", _.INJURED ? 2 : 0]);
```

h2: آه، نمی‌خوام ناراحتت کنم!

`publish("act4", ["hong_to_alshire",4]);`

h2: فقط یه چهره‌ی آشنا رو یادم اومد، همین.

```
publish("act4", ["hong_to_alshire",5]);
publish("act4", ["alshire", 4]);
```

{{if _.TOP_FEAR=="harm"}}
s: آآآآآ می‌دونستم! اونا یه روانیِ خطرناکِ هراس‌زده‌ان!
{{/if}}

{{if _.TOP_FEAR=="alone"}}
s: آآآآ اولین برداشتی که از ما داشتن «شاهدِ ترومای من بود»! یعنی از ما متنفرن!
{{/if}}

{{if _.TOP_FEAR=="bad"}}
s: آآآآ ما باعث شدیم یکی یه رویدادِ تروماتیک رو یادش بیاد. حضورِ محضِ ما به بقیه آسیب می‌زنه.
{{/if}}

(#act4e)

# act4d_yes

```
publish("act4", ["hong_to_alshire", 5]);
publish("act4", ["bb_to_alshire", _.INJURED ? 3 : 1]);
```

b: صبر کن آدم، به نظر می‌رسه ناراحتن.

```
publish("act4", ["hong_to_alshire", 6]);
publish("act4", ["bb_to_alshire", _.INJURED ? 2 : 0]);
```

h2: آه، هیچ فشاری نیست!

`publish("act4", ["hong_to_alshire", 4]);`

h2: فقط می‌گم، اگه خواستی می‌تونی اینجا بشینی.

```
publish("act4", ["hong_to_alshire", 5]);
publish("act4", ["alshire", 4]);
```

{{if _.TOP_FEAR=="harm"}}
s: اونا دارن *زیادی* مهربون رفتار می‌کنن! مثل تد باندی، قاتل سریالی!
{{/if}}

{{if _.TOP_FEAR=="alone"}}
s: اونا فقط دارن خوب رفتار می‌کنن! هیچ‌کس *واقعاً* نمی‌خواد به ما نزدیک بشه!
{{/if}}

{{if _.TOP_FEAR=="bad"}}
s: آآآآ ما همیشه بقیه رو به راحتی نمی‌رسونیم! ما یه لکه روی زمینیم!
{{/if}}

(#act4e)

# act4d_no

```
publish("act4", ["hong_to_alshire", 9]);
publish("act4", ["bb_to_alshire", _.INJURED ? 3 : 1]);
```

b: صبر کن آدم، ممکنه داریم ناراحتشون می‌کنیم.

```
publish("act4", ["hong_to_alshire", 3]);
publish("act4", ["bb_to_alshire", _.INJURED ? 2 : 0]);
```

h2: آه، نمی‌خوام بی‌ادب باشم!

`publish("act4", ["hong_to_alshire", 6]);`

h2: فقط یه کم وقت نیاز دارم که احساساتم رو پردازش کنم. لطفاً به‌عنوان ردِ شخصی نگیرش.

```
publish("act4", ["hong_to_alshire", 7]);
publish("act4", ["alshire", 4]);
```

{{if _.TOP_FEAR=="harm"}}
s: دارن چه افکارِ مریض و پیچیده‌ای رو پردازش می‌کنن؟! چه آرزوهای تاریکی قلب این روانی رو پر کرده؟!
{{/if}}

{{if _.TOP_FEAR=="alone"}}
s: ما به‌صورت شخصی رد شدیم! هیچ‌وقت دوست‌داشته نمی‌شیم!
{{/if}}

{{if _.TOP_FEAR=="bad"}}
s: ما پردازشِ احساسی‌شون رو قطع کردیم! حالا برای همیشه تروما می‌گیرن و همه‌اش تقصیر ماست!
{{/if}}

(#act4e)

# act4e

```
Game.WORDS_HEIGHT_BOTTOM = 195;
publish("act4", ["alshire", 6]);
```

s: فرار فرار فرار فرار فرار فرار فرار فرار فرار فرار فرار فرار فرار فرار فرار

```
Game.clearText();
publish("act4", ["hong_to_alshire", 0]);
publish("act4", ["alshire", 10]);
sfx("pop");
```

(...1001)

```
publish("act4", ["alshire", 11]);
sfx("alshire_run");
```

(...2601)

```
publish("act4-out-3");
Game.WORDS_HEIGHT_BOTTOM = -1; /* reset */
```

(...1201)

`publish("act4-jumpcut-hong");`

h: هوم. اون عجیب بود. فکر کنم تو سرشون چی می‌گذشت.

`publish("act4", ["hong_closer", 2]);`

h: به هر حال، داشتی می‌گفتی؟

```
publish("act4", ["hong_closer", 1]);
publish("act4", ["bb_closer", 6]);
```

b: اه، یادم رفت؟ یه چیزی درباره‌ی تیم و کار؟

```
publish("act4", ["bb_closer", 0]);
publish("act4", ["hong_closer", 3]);
```

h: ¯\_(ツ)_/¯

```
publish("act4", ["hong_closer", 1]);
publish("act4", ["bb_closer", 4]);
```

b: می‌گن باید با احساساتت «صلح کنی»، انگار احساساتت *جرم جنگی* هستن.

`publish("act4", ["bb_closer", 7]);`

b: ولی من می‌خوام بیشتر از صِلح باشیم! می‌خوام *متحد* باشیم!

`publish("act4", ["bb_closer", 3]);`

b: می‌خوام یه سگِ نگهبانِ خوب باشم. درست مثل اینکه گرسنگی و تشنگی زنگ‌های خطرِ نیازهای فیزیکیتن،

`publish("act4", ["bb_closer", 8]);`

b: می‌خوام زنگ خطرِ نیازهای *روانی* تو باشم – نیازهات به امنیت، تعلق، خوبی.

`publish("act4", ["bb_closer", 1]);`

b: ولی... من تو کارم گهم، پس نیاز دارم که آموزشم بدی.

`publish("act4", ["bb_closer", 4]);`

b: من نه «همیشه معتبرم»، نه «همیشه غیرمنطقی». فقط... دارم بهترین تلاشم رو می‌کنم. پس لطفاً،

`publish("act4", ["bb_closer", 30]);`

b: بهم کمک کن که بهت کمک کنم!

`publish("act4", ["bb_closer", 6]);`

b: هرچند، به یه سگِ پیر یاد دادنِ ترفندهای جدید *کمی* طول می‌کشه. شاید *سال‌ها.*

`publish("act4", ["bb_closer", 3]);`

b: و بعضی وقتا به عادت‌های قدیمی برمی‌گردم.

`publish("act4", ["bb_closer", 2]);`

b: به سایه‌ها پارس می‌کنم. با کلمات می‌ترسونمت. حتی ممکنه تصویرهای مزاحمِ... چیزایی بهت نشون بدم.

`publish("act4", ["bb_closer", 9]);`

b: متأسفم! من یه سگِ پناهگاهِ زده‌شده‌ام! سگ‌های زده‌شده بعضی وقتا رو تختت می‌ککن!

`publish("act4", ["bb_closer", 4]);`

b: ولی اگه باهام صبور باشی... و فقط بمونی و پیشم بشینی...

`publish("act4", ["bb_closer", 8]);`

b: شاید بتونی این گرگ رو رام کنی.

`publish("act4", ["bb_closer", 0]);`

`Game.clearText();`

(...1000)

`Game.OVERRIDE_CHOICE_SPEAKER = "h"`

[سگِ خوب.](#act4f-pat-bb) `Game.OVERRIDE_CHOICE_SPEAKER = "h"; publish("act4", ["hong_closer", 2]);`

`Game.OVERRIDE_CHOICE_SPEAKER = "b"`

[آدمِ خوب.](#act4f-pat-hong) `Game.OVERRIDE_CHOICE_SPEAKER = "b"; publish("act4", ["bb_closer", 8]);`

# act4f-pat-hong

```
Game.clearText();
publish("hide_tabs");
Game.FORCE_CANT_SKIP = true;
music(null,{fade:0.5});
sfx("youbothwin");
```

```
publish("act4", ["hong_closer", 4]);
publish("act4", ["bb_closer", 13]);
```

(...501)

`publish("act4", ["bb_closer", 14]);`

(...501)

`publish("act4", ["bb_closer", 13]);`

(...501)

`publish("act4", ["bb_closer", 14]);`

(...501)

`publish("act4", ["bb_closer", 13]);`

(...501)

`publish("act4", ["bb_closer", 14]);`

(...6501)

`publish("act4", ["bb_closer", 15]);`

(...1001)

(#act4f)

# act4f-pat-bb

```
Game.clearText();
publish("hide_tabs");
Game.FORCE_CANT_SKIP = true;
music(null,{fade:0.5});
sfx("youbothwin");
```

```
publish("act4", ["hong_closer", 4]);
publish("act4", ["bb_closer", 10]);
```

(...501)

`publish("act4", ["bb_closer", 11]);`

(...501)

`publish("act4", ["bb_closer", 10]);`

(...501)

`publish("act4", ["bb_closer", 11]);`

(...501)

`publish("act4", ["bb_closer", 10]);`

(...501)

`publish("act4", ["bb_closer", 11]);`

(...6501)

`publish("act4", ["bb_closer", 12]);`

(...1001)

(#act4f)

# act4f

```
Game.FORCE_CANT_SKIP = false;
publish("act4", ["bb_closer", 16]);
publish("act4", ["hong_closer", 5]);
```

{{if _.fifteencigs}}
b: آآآ تو هنوز داری تنها می‌خوری پونزده نخ سیگار آآآ
{{/if}}

{{if _.parasite}}
b: آآآ تو هنوز موقع غذا خوردن کاری پیش نمی‌بری ما انگلِ جامعه‌ایم آآآ
{{/if}}

{{if _.whitebread}}
b: آآآ تو داری نونِ سفیدِ بیشتری می‌خوری آآآ
{{/if}}

```
publish("act4", ["bb_closer", 18]);
publish("act4", ["hong_closer", 6]);
sfx("yaps", {volume:0.6});
Game.FORCE_CANT_SKIP = true;
Game.WORDS_HEIGHT_BOTTOM = 205;
Game.FORCE_TEXT_DURATION = 90;
Game.FORCE_NO_VOICE = true;
```

b: واق واق واق واق واق

(#credits)
