from tv_class import tv

tv1 = tv(1 , 10)
tv2 = tv(3 , 20 , True)

tv1.set_channel(20)
tv1.turn_on()

print(tv1.on , tv1.get_channel(), tv1.get_volume())

tv1.volume_down()
tv1.turn_off()

print(tv1.on , tv1.get_channel() , tv1.get_volume())
