# intro

`SceneSetup.intro();`

# intro-play-button

(...51)

```
_.PLAYED_BEFORE = !!window.localStorage.continueChapter;
```

{{if !_.PLAYED_BEFORE}}
`Game.OVERRIDE_FONT_SIZE=30;`
{{/if}}

{{if !_.PLAYED_BEFORE}}
[#play1# بازی! #play2#](#intro-start) `publish("intro-to-game-1"); Game.OVERRIDE_CHOICE_LINE=true;`
{{/if}}

{{if _.PLAYED_BEFORE && window.localStorage.continueChapter=="act2"}}
[_ادامه_: مهمانی](#act2) `publish("LOAD_GAME", ["act2"]); Game.OVERRIDE_CHOICE_LINE=true;`
{{/if}}

{{if _.PLAYED_BEFORE && window.localStorage.continueChapter=="act3"}}
[_ادامه_: مهمانی دیگر](#act3) `publish("LOAD_GAME", ["act3"]); Game.OVERRIDE_CHOICE_LINE=true;`
{{/if}}

{{if _.PLAYED_BEFORE && window.localStorage.continueChapter=="act4"}}
[_ادامه_: ساندویچ دیگر](#act4) `publish("LOAD_GAME", ["act4"]); Game.OVERRIDE_CHOICE_LINE=true;`
{{/if}}

{{if _.PLAYED_BEFORE && window.localStorage.continueChapter=="replay"}}
`Game.OVERRIDE_FONT_SIZE=30;`
{{/if}}

{{if _.PLAYED_BEFORE && window.localStorage.continueChapter=="replay"}}
[#play1# دوباره! #play2#](#intro-start) `publish("intro-to-game-1"); Game.OVERRIDE_CHOICE_LINE=true;`
{{/if}}

{{if _.PLAYED_BEFORE}}
[انتخاب فصل](#chapter-select) `Game.OVERRIDE_CHOICE_LINE=true;`
{{/if}}

[(هشدار محتوا)](#intro-play-button) `Game.OVERRIDE_CHOICE_LINE=true; publish('show_cn');`

# chapter-select

`publish("HACK_chselect");`

[۱. ساندویچ](#intro-start) `publish("HACK_chselect_end"); publish("intro-to-game-1"); Game.OVERRIDE_CHOICE_LINE=true;`

[۲. مهمانی](#act2) `publish("HACK_chselect_end"); publish("LOAD_GAME", ["act2"]); Game.OVERRIDE_CHOICE_LINE=true;`

{{if window.localStorage.act3}}
[۳. مهمانی دیگر](#act3) `publish("HACK_chselect_end"); publish("LOAD_GAME", ["act3"]); Game.OVERRIDE_CHOICE_LINE=true;`
{{/if}}

{{if !window.localStorage.act3}}
[۳. مهمانی دیگر]()
{{/if}}

{{if window.localStorage.act4}}
[۴. ساندویچ دیگر](#act4) `publish("HACK_chselect_end"); publish("LOAD_GAME", ["act4"]); Game.OVERRIDE_CHOICE_LINE=true;`
{{/if}}

{{if !window.localStorage.act4}}
[۴. ساندویچ دیگر]()
{{/if}}

{{if window.localStorage.credits}}
[۵. تیتراج پایانی](#to-credits) `publish("HACK_chselect_end"); Game.OVERRIDE_CHOICE_LINE=true;`
{{/if}}

{{if !window.localStorage.credits}}
[۵. تیتراج پایانی]()
{{/if}}

[(منوی اصلی)](#intro-play-button) `publish("HACK_chselect_end"); Game.OVERRIDE_CHOICE_LINE=true;`

# to-credits

`stopAllSounds();`

(...101)

(#credits)

# intro-start

(...500)

`clearText()`

n3: سلام! این بیشتر یه «بازی» نیست، یه داستان تعاملیه. امیدوارم خوندن دوست داشته باشی، رفیق!

n3: قبل از اینکه شروع کنیم، بگو *دوست داری* چطور بخونی؟

`publish("show_options_bottom")`

# intro-start-2

n3: عالیه! نکته: همیشه می‌تونی با آیکون ⚙ پایین، تنظیمات رو عوض کنی. ضمناً بازی آخر هر فصل، خودش سیو می‌کنه!

n3: حالا بریم سراغ داستانمون...

`clearText()`

(...1000)

`publish("intro-to-game-2")`

n2: این یه آدمه

(...600)

`clearText()`

(...300)

`publish("intro-to-game-3")`
