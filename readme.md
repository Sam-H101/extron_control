## Wrapper for extron ssh commands

### Usage:
```buildoutcfg
    e = ExtronControl()
    e.set_routing_ports('one', 'three', e.get_units()[0])
    e.start_recording(e.get_units()[0])
```

### Command Reference
* set_routing_ports
    - this sets the channel inputs to record with. 1,2,3,4,5
        - Top always has 1,2 
        - Bottom depending on unit will have 3, 4, and maybe 5
        
* start_recording
    - this starts the recording with the wanted unit.

* stop_recording
    - this stops the recording with the wanted unit.