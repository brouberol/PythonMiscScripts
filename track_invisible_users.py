import xmpp
# Not 100% fonctionnal...
# Qui est invisible parmis mes contacts Gtalk ?

 
#constants
USER_ID = "rouberol.b@gmail.com"
PASSWORD = "aboutblank991"
SERVER = "gmail.com"
 
jid = xmpp.protocol.JID(USER_ID)
C = xmpp.Client(jid.getDomain(),debug=[])
 
if not C.connect((SERVER,5222)):
    raise IOError('Can not connect to server.')
if not C.auth(jid.getNode(),PASSWORD):
    raise IOError('Can not auth with server.')
 
C.sendInitPresence(requestRoster=1)
 
def myPresenceHandler(con, event):
   if event.getType() == 'unavailable':
     print event.getFrom().getStripped()
 
C.RegisterHandler('presence', myPresenceHandler)
while C.Process(1):
  pass
