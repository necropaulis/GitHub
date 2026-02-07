setcpm(60/4) ///cycles per minute 60BPM, 4 beats per bar
const Roland = "tr900" /// Instrument
$: s("bd:2!8")///high hat #2, 4 beats per cycle
.s(square)
.gain(rand.range(0.5, 0.2)) ///changes gain at a random rate between 2 values
._punchcard()
  
  
  ///Visualizer

$: s("bd:4!8")
  .slow(6)
  .gain(.5)
  .s("sawtooth")
  ///.fast(1.5) ///speeds up
  .degradeBy(.4) ///loses random notes by a certain percent
  .rib(100,1) ///repeates a pattern - first number is seed 1-999, second is how often
._punchcard()