setcpm(120/4) ///cycles per minute 120BPM, 4 beats per bar
const Roland = "tr900" /// Instrument
///$: s("hh:2!8") ///high hat #2, 4 beats per cycle
.gain(rand.range(3, .7)) ///changes gain at a random rate between 2 values
._punchcard() ///Visualizer

///$: s("hh:4!8")
  .gain(.5)
  .fast(1.5) ///speeds up
  .degradeBy(.4) ///loses random notes by a certain percent
  .rib(700,1) ///repeates a pattern - first number is seed 1-999, second is how often
._punchcard()