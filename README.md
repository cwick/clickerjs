1. Run `touch_remote_service.sh`
2. Run `pairing_server.py`
3. Run iTunes, find the remote device, and enter any 4-digit PIN
4. After iTunes successfully pairs with the device, run `./dacp_send.sh "login?pairing-guid=0x0000000000000001"`. That will return something like:

```
 mlog  --+                                
        mstt   4      000000c8 == 200     
        mlid   4      033c16bb == 54269627
```

Here, `54269627` is your session ID. Include it in all future requests.

Now you can send commands to iTunes. For example, to make iTunes pause playback:

```
./dacp_send.sh "ctrl-int/1/playpause?session-id=YOUR_SESSION_ID"
```

For more commands, see here: http://dacp.jsharkey.org/
