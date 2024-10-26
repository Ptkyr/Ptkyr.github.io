#import "@preview/rubby:0.10.1": get-ruby

#set text(
  font: "Junicode",
  size: 10pt
)

#let ruby = get-ruby(
  size: 0.5em,         // Ruby font size
  dy: 0pt,             // Vertical offset of the ruby
  pos: top,            // Ruby position (top or bottom)
  alignment: "center", // Ruby alignment ("center", "start", "between", "around")
  delimiter: "|",      // The delimiter between words
  auto-spacing: true,  // Automatically add necessary space around words
)

#let kanji = ([裁],[判],[断],[定],[義],[理],[解],[放],[送],[信],[用],[意],[図],[表],[題],[材],[料],[金],[魚],[醤],[油],[絵],[本],[部],[活],[動],[機],[能],[率],[直],[接],[触],[発],[売],[買],[収],[容],[疑],[問],[責],[任],[命],[令],[和],[平],[気],[配],[置],[物],[価],[値],[段],[落],[雷],[雨],[天])

#let right_readings = ([さい],[ばん],[はん],[てい],[ぎ],[り],[かい],[ほう],[そう],[しん],[よう],[い],[ち],[ひょう],[だい],[ざい],[りょう],[きん],[ゆ],[ゆ],[ゆ],[え],[ほん],[ぶ],[かつ],[どう],[き],[のう],[りつ],[ちょく],[せつ],[ふ],[はつ],[ばい],[か],[やつ],[よう],[ぎ],[もん],[せき],[にん],[めい],[れい],[わ],[へい],[け],[はい],[おき],[もの],[か],[ち],[だん],[らく],[ゆき],[あめ], [])
#let left_readings = ([], [さい],[ばん],[はん],[てい],[ぎ],[り],[かい],[ほう],[そう],[しん],[よう],[い],[ち],[ひょう],[だい],[ざい],[りょう],[きん],[ゆ],[ゆ],[ゆ],[え],[ほん],[ぶ],[かつ],[どう],[き],[のう],[りつ],[ちょく],[せつ],[ふ],[はつ],[ばい],[か],[やつ],[よう],[ぎ],[もん],[せき],[にん],[めい],[れい],[わ],[へい],[け],[はい],[おき],[もの],[か],[ち],[だん],[らく],[ゆき],[あめ])

#assert(kanji.len() == right_readings.len())
#assert(kanji.len() == left_readings.len())

#let foo(i) = ([], ruby(left_readings.at(i))[\u{202F}], kanji.at(i), ruby(right_readings.at(i))[\u{202F}], [])
#let line = array.range(1, kanji.len()).map(i => foo(i)).flatten()

#grid(
    columns: 5,
    row-gutter: 3pt,
    ..line
)
