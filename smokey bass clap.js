setcpm(120/4)
const Roland = "tr900"

$: s ("bd cp bd cp, hh*8")
  .lpf("<1500>")
  .room(.75)
  .cutoff(750)
  