import re

test_input_string = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""

input_string = """fivethreeonezblqnsfk1
two74119onebtqgnine
jrjh5vsrxbhsfour3
tn5eightfncnzcdtthree8
kpmrk5flx
fkxxqxdfsixgthreepvzjxrkcfk6twofour
dqbx6six5twoone
glmsckj2bvmts1spctnjrtqhmbxzq
7sixthreerzmpbffcx
zhss9gfxfgmrmzthreefivevpkljfourtwoeight
6tfzvrbkfour
sevenfive66five851
drsgdrrgscqmsggrgq1fsqjhtkkrltt
3ftptvzhvrm5
twoeightninemfsztp2gbqkpgqvzt6threekcdcp
four156
959157fourfive
sixthreetwo87one7fourdbczdbjcc
lshzfive7
38ninethreethreesevensixeight
z39hpppnncfivenbkc
9ninefivevnbrrfrfjfivetwo
fzgnjsz2nine9
fnhksixfour1six81
vkkxbgcqzqflgsvgkkkpfp9five58stsix
eight26sixsghd
7zvrjkcrrgbsix
tgdf38fpcssixeightcjtfour
tcrqkxkptrtt5fdblcldfoursix
9qpmknkbtxsfourd
8948twosix9three8
vpbjslqkpbxkpfiveeight1mzjmhfzl
187jccxsbqtcjtwo1
sixfiveonefour637three
stjbeightsixdfnsppjrgfdggqzjx6cplvznllsgtwo
3lrznqgc85seven3
1eightfourfourmgxhdp51slrszbxmhthree
two3hj
zgnoneightseveneightseven5d2fivefourjp
ldjzhninetwokxlkbbzcngssdqphlrc51
qvhtfhmltt61lss
lfmnhxmhschzrtntwotwo7twovkl8two
vrpplrtqxvssgnvdf8
dzrnnphfl451
two7pgbsixlkmseven
rplqnj5oneseven
2fourfourchd7
threesixdpslzdft3hq
three4bqhlckrlgeight2lbdvcggfqd
ninefive6zqhgfhfdnk
2one9five2
1ftsjdfmnkvlx9seven
four1zsztlvnhcjtvmrlthree4kpztfzqjtdplfxpqlskh
6zfrhkckfvxsixtjgtnmcx
eightfourcppgkrmtn3chqxgscpd1
6threegxdrv8
mstpbscvjrc5twozjtdxhckrfsnzsdm
twolhntgone5
vtrktlkrqslcdnlslthree5
mfkrfournine4knmmmghnsixxrmzhcsix
2hfkbthree
nine96
threeqglpgvxgsdfgbctdm1
1threechctd2tnm
nfgrzrz494twogbrbcpvnine
two5fdnksffour
19threeninefive7xzmtzmkpjmnine
six37sixninejqt
kk28rqmlshb4
qmhlxonefbgcrclbf4sqtcpmtlzdzhg4b
leightwoplxmgrcjcxrfqncvjfdvpgckmqfqsfqjthreefour2djnsvctlt
nseven7dphcjx36twosevenfour
rdjkdfivetwo5sixfourfjkzbpjx
fiveeightcdttxrxjxchf6oneddnpdgxlrpqxrgqtcbgdqhzzsxdt
5blgzg
ninetdfive7
eight9qldkxsevenfour
onegprdninefourgndvp7
four13znsmhvtmfour
threeqnvl9zzzfoneeight
sevenzkbxghrgftsxfndhlrcxlcj64
kjlmclkqkjl76eightxdlonef4
7oneninefive4fkonerjpzpq
248seventwo6six8vbfb
8khtwojr
hssqpxptsb2
3qcf
93xrm
twoscjr4jtkzxvlfnkltzxf63
cltkcrh9jnkvjsfmtlszkvstzp
3sjtone9cznjhnkzmc8
qcjmxqfhlsevennine6
456rrkxxlfrhk4
hthreefrq7lnng
427seven
slq5vtrsninesix5
5two94bone4
six73one
fournine757fdgkbppx3
93onefive967vmtmbnjm
bhcktnzlsghvdl9eight
fournine9threenineeighttwo
21cngsixsix
5nhgtsxdninedvqktrqn
8tbnznrbg21
6rjsxftdjgf29
zdfourqtrjqzglq4six
ninemxhcjfbprlts1six
jnmzkfivefive2six2ninegfntlslsgp
fouronetwo7seventwoeight
sevenfoursixfive2sevenffr2
8bhpx4seventwo
ljclbvmlpeight754two14
eight11oneonefivesixsix1
26ddmfrzzd6qdnvpqjpvdseven
vjgjpjtceight36fivesixpdrrlqpmk
three349mzhnlg
tmrxzcrdc9eightninephdq
two11rtlddgh
9fourtgsixgppd4two
34onenineeighteight
4eighthcx92mhrpjfndt92djgtmmnbv
nine771two9seven2drflmd
hxvsgpcxgkh4twollmbbbprxd349pb
twobpbp2eightmjlhrgc
fhnnf37sixone5mdvhhssvg
cknbvdmtcninemmhtrhmx2
one93
onervc8oneeightsixfour3
fournine2
knvjjvskmsixsixlvzt5sevensixmmthree
2sfour
29zqnxnqphflltqh
23eightptpspjtbnninesixfivedhfnmqjd
29jgghdf8
meightwodccsxmc4nvq3sevenqdshf
fourbbnqscg3
onetwo2fivef54
nctbrzqsdljjsix5
5mblhxfqfns9nine
6gbone8
6gd9
eight5nrzhl4sixseventrvtwokg
r21jjnine
mhfsgvcck5
six92cdngxmfive
pdmmpzgxc1fourzbmbgtthree
rdhppfnk8
fiveone4cf96qprdgcrlhvsixhznbbbh
two4eightsjzrlkhgbrxzs
nzhqbzfxchvtbs9sixnfmhpc
785eight
hxgdntgnmr8
xsrxnx4tqzqgv62
six9ssevenkdqrcnjgvn
dfvcznvxqd6twozs6xsfvtmnvln7
rhlseven2957vtmpgczngccrmggvtf
gfbsfpn9s
jxtwonenine39eightpzmbdff3
66pmgzhgffp
9cgjmfbgsrg89
858tknqxhrgfournine97qrlvf
7fiveonedzbmblrtqfoneightkc
7gsfvvvfive72gjfbgk5
1rsscgplc6two4fvxfgnkghfthreejddxmtsxjzmnhgcc
537eightthreeonenineeight2
tzhgg26one
qxqhmhdhgqktsvkbkfiveonenzcjfgvnlms4
ninenctkgtseightxkjlmkjpbd837
5xjdl16cjthtvj
5threesevenvnthreeqkcd2xkfhprfgdzseven
pkqlqdvmsmsevenrmhhjtdnneight5
cfqoneeight1psqjtgng34one
dnvdnstxrsgktsfk9
eightjbdcdxpnzm736xh9
z5
x5xffv
3ggnbr
82dlnzszhpvjftdt
gkthhvsix7rfbrmnzvmlbsk
nineeighttwotfjndlrdpmvfbhs2
9fpxsgdj5785nsxn5seven
qhs1ninethree
86pcqdkg8onefive5seven
mlteightwogeightsmmfvtwo6
sixonefourpnnrbl9
xstrnmzzjrsmbdone6xt
four777hkzrdclsrdfrqkkkh6
xzfnndt546lvngqlghtggcrqfour
svqlsxtlfvqqzjq2
167cffstwo
7ninefive5three92shmpzx
eight1threefive8fivetwoeight1
four7eightone4onelcrb7eight
vzfrfxzzfzmldsixfour2hfpln
6one8sixninetwoner
nsqhnflqjnqvdgvfive21
9sixeightqjhpdv
jstwonethreeninepfkkzvbzcknkmbcbsf6
3five5
499jvmmrfzkmbppzcm
vdpvj3nineeight7
three2fdeight
rtwo39seventhreett
two68sixeighttwo9
9kmmftsfgjm284gmmlsfvjk
five7gtbpfourthree9xbfttssrsix8
oneeightmbbklndlztwo9nine18
nthreesklqbkrxrmxkfpfprbjl3kqrgqtvgxdbcjnn
six9sevencnn5
sevenone2
three794sevenlqcbz
fourdcfour466twonesz
2534
qv5cm4rpcjkd
fivehmvssv6
twopltxmsevenfkfour956xvgxbbckqn
94txltmgz72fkcgcdkbrkbkfpnfck
seven9seveneight46
457k
fhvdpgxpone18c9lnfnp4two
sixfive458x7
eightdjnlvvsevenrnsxrbxqptrvhgnggv77
qrvrnzxjkj5
seven4two
twofivelcrfkzck8three9jcdxvnrsevenvkg
77sixrjqcmrhktb
ht9krsfghfrk6
zfqsix77
gjxzhgxzmdrczfpqlbp1562njqb7
79three4b79
twoqgxjkvmfivevknkxjp5nv3
hjbzznfourfour8fivemkqthree2
7ninecjtnr2rnpjsxnine
73mzgdbvrjjpzzxmgbjcdqjx29three
kskfgnxbjg97twofourhxpfqxqfivethree
fivermxblcb2one4
ninefvkfplbsixoneoneeight2vnns
8q3foursevenlvmtrrqtsix
2three54
jf6fivesixmbnhjdt
2mpkmrfqctzrfour
six4nineh
2fqseven1nthreethree
8nine4rhdfive
zczjmlslrmjbgrmbpqb3
sixpstrxqtdtwofour7ninefive5
kzkftdrqzthvx56oneptlvfzvsfiveseven4
p71dmsnoneldx
nine9twofour5sixzbshnn
6qsbkgsxrs66one7rnkqzkqfvkhtm
jnzzxbtt1kctmsdplhg4
pvbnkszjpmeightsixmxjxdprgcsix8zntghmvrl
brninesevennine3
threedgbqjxhneightchxnvnptwozzfrqqtmmvhcksmjk49
sixslxtwo2z7grtgdnffc
936797pbgtlpkttwokdqlfpbcmv
six99fsrnbpdthreefivejpdcvgt
one8sixsix4jqsvsqnjnxqvh
dsjkbmq1mghlstwo
42two
qbqgt2ninemghghninebdppsjcb
bmfmbzg36nine7mqljk6onenine
763
five8ninethreesevenllmjskvbtlngstbmhhqhf
2klljtwothree3
one2jgrqmprg197
1fcjfbxonefive
171
five4zxbqc2eightseven6eight6
sixpkqvvlqkdkhqdseven4rjq27rrjpxl
79lcsrsix7twolnjjjqffhshfjshkrfeight
mczbvstsml22vjseven3gvf1
two6sixonetwovntpsbfgdk7snzxrxdmhtgj
2ksgklnnine6kdfg
6seventhreevskblmp
9mptsnrpdqldltwo
52cgvgnsk3one9
sixfive4kstqckhgdd
vxhtwone7eightninebvlpkcmfourone5four
4hnhlr83three3threeeight
1eightfive
36fbtgvdfnine9
eight6ljtbkp
eightsixsix96bvjnxzjjchldtc6
jbckzxc5five
vghptkb7onejnrnfftgthree
mztxz39six
7rmchptmrglsix21two
91tmvvktwo
seven9fqmfkgthree9sevenfive6
jrcj441
1nine9
674foursncnphhnd92
fsfrcgsonefivelpkz5threesnrzzvxcdn4fl
8zrlf5pvmzshrjkdgfkpzmgp
cflcrf8four9
6fourkjhtlfrlpmjc95
968fourzqhkzxtxeight8
onefivethree6qxrpxkt
four46vvdvrkgv
five9six
1nine8
bvqlzpjrmckxpgdfz7
rrvv27
9three8gmsbrrxzh4dxvvstrkzf8nine
frnqrxzcfivesix747
5threek7eighteight9
four4rrsqsm
twoeightsix5zmdmcxcfdnrnjjsixmfqpvndkctzdv
8zvbnthreenvplvljj
srfkl8twofive
82njdktmcckrjf39
qqgmhfourthreeeightjjxfour68three
fourthreenine5
9nsfkfcdqcbrbdh4ninetwofiveseven4
7fivetwo
2lssdgdvhl
fouroneqmffoursix9eightwokv
4cjmsixqhddpcsngvxqskkbmseven
266bfxtxpkxcxthree2ktmtddmfg
five6ninebgzmgqbsttf3vhn
pqmgcchhqrpsljbvx1fourmhzszhdmfznine
jlxlcqfc1bgqjsvxpbn
eightfxpnxckzqxseven6llfvqqbhdd1ninesix
threeflgkjrnrmr4xpxfhhl
6pvszcmrmtbfhlnmgmqxnqvntg96
cgnp8ffnxlpmblonethreeqcqnx6
zjvpxg3ccmkxtzhlx
7vgpflkfdkvktfhxgf8hcgxzz
4cmhfccrttfive
12twofour
jrgoneightnddmmchbmmklk847three
threefourgbsjmmrznlmgttq3zncprp8
ntqpbkvr3xkgqgxjh82
nine9five
n1eight979
8fzvjmmnhd2five
6vxmbqsvzt
22fftjtpv84sevenn
twoone7slfhztpc7bfjptdzj
91fiveddprnkzprseven
fivetwo8dssgjmpmvsixps5
pv9eightfourhgklds4pfnxmtpmzrmx
vfjfd4sevennljkxxrz
3threesfourfourbftwoksclvtxmvmq
seven7fsj165
77sixkqsdpzxv9
1fourninemqxqc412
pmdmtthree1sljpn99three
zvqvhhbrg76bfbldtwoeight
sixbh5two5two8
fivefournjdlbggpsbn1threevzqktlbm8
glzqmznfiveninesixkscdflhqj9rjnjt
hjgbncf9
zdnf7
six6fourjghzroneightf
6zxvqqxrc
d6
1txhlrsnbk97fivelvqjxeightfour
hthdvd35six7
ninedrc3one
eight28nine1vjm3nine
zrnninesevenvftnjl1pdfgkdhmjjgmpgxkjttwo
threelhnhfxkeightsix7
gjqng7two46pzxcsbgnv
sixcdj9ghqlbsnpbninesevenxdzkqxdfdrlfpgnpg
nineninethree3twovhjhjgfive8
ldgzxftnninenine82
zxvtgsfiveone1sevennine4rfh
1318khksmlfv9sevenfvhrt2
vztwoneseven1rb
457threeninedmffxznlpb8
five7eightcvgcmqkctclnjsnfourvqptsnpph4
pftwonexgrzdvq65
64hfptjtqztlv
fmxfjg686fivettfgd
hpbqxfour6two86nmrhgkeight
3skzmdggpnxsix5four8
sixfour7smh6gbbphmv8xrrrsns
5bjvmxml3threephlfnbpfxq
9zlrdnxvzffghrqhsixfcsrtqvfone
61hmdmjfv36eightthree9
78six3crj4nine7
fourqhtvfbpx9hcvmzmdjrshkhrthree
threeninehbcgqmxknine8z
17csdthtzrsqnssxqfivesttdfzxrkhnine3
9eightpcflcqfhveight3
hbvkzz9seven
6seven6
eight3two16tlnsmxpqbn
fjqhctnjhk4fourcgxfhffrk98grx1
sjkpr34
hvlh2five8fivendxh7three
onethreed12jvnk1
fivetwo1rtscxhkqpvtxkmjccbcvl549
5qvmvft
nine9cpqzbvhseven9mtjk9seven
znrpx47two67six5
xnqk5fourp4tflgmbvhlxsixfive
3fivesevenrzeightbhfvhrh
qzmbljhone8fpmkrrrhvdbqvdthree1
rfzfztn83jrtnn3five
29one5fiveggrhlvtvtz1
onennczlkx3twozjdlblqcvhtwo1lrvtx
mhmrtmjlffjlmhfour45two
bvjnzxbmfninefour94four
glrcmgthreesix6eightxgzx3
six7v4onevptsdghxqblrpblng
7nine6sevenoneone
pf8oneoneightjgl
5dftcf8fourfive8ljdkhjxd3
nzqnbpssix54ssmsnthreex
8fourpbxtvcmsvrvkcms2zvvvmkp
mv9eightone
2lvthreekbfjj3glbrlpxsqlkdksixseven
twotsvcqfoursevendfsqk1threeone7
fivefsphdxqlpds91kkfqone
eight5two9
fourfour7tfxr
2czjhjsrrzc
ninetsrzqvldgn9fivefive
fivetwothreevcdvqnv2zhmtmrqvv2
nine9tqkhxsthree2eight63
bneightwo8kpkkgbxgnineqjkt4fiveninesevennine
rvhjzveighthqdgzhfcbnxztf25sixfour
8four4six
rjsgxsjqrq1pbzhfxqvphvnd67kvt
sixnine6
xnvfgvcs7
3sevenoneone3
btmnrqcphpcxnhtwopvlthreeseven9
991
3ninepqhq9mtwo
eightfmfkfvmtwofoursix2
two48
bone5phdjdlseven
ptfxfdkninefive6sgrjhxksft6
nine9eight
2pkbv
lhqeightwoseventhreegtpvhsixdgseven8vlkkl6
j8nzlqctlbffonegzcvpjksmr1ninetwo5
f93fmgqllzf5
mtsdrqzqrkthreesnjxkdjlc5fj
95onenmqrzbkksevenfour5five
six8threetkzqrs
two9twooneone2rdkdtlttj8
srjlgxreight8fiveoneightt
7fourxtcj
threelrqhtjtts9zsix1jvrkkzn8
6xxqlzkgfspv
zltbp8
four3seven6mhqtln342
9eight7rrseven8zmcqd
mlgcbjhxjeightqxxxb4seven
3nfivedgpvxprzvpbftplgtfivefour
ninenhxjqzhhhl1three99
fivetptfpone89ponefourjxmdrjkrleightwoh
3tspjckb
9four39gvlmp5
twotwo89
mboneightgjjrxxxkmmhprxptqtvseven754gjjr
pdgksxnkqj7fourdtjlnjs3four4
3qkkbbfkvnninencbvnvztmnfpbsix8one
seven2jqljbktgzvr
fourdv5onesix8five8seven
5sthtkqk5
tlpds3
tvzflpzpgsl2hcpsgxxtgqeightfoureightoneone
8gjflqxf26rfour
578vsxmdtleightsix
four2two6
5onetqhsfourtwosix
1xj5fvmftprrcqvmcj9
qzbptdttbqseven6
8l
ninejsfdnfl85fpjgcmkqvmfivetwoeight
kcmrgnljhpfv2jjrfcvdqsixkjhlfnq
cmlvvonelmkfbt3qfdgz5
9hnsjjgdd4mvksevenfzplpczbbonetwo8
zone3
cthtrxb39393
4nine54six4txtpcz
m1bgfeightqjhvlrlfj
3199
one6nineeight5vktwo9kgfjhktlgb
2cpgtrfourtblzrhdlvdq7fourtlpvjkpn
qpfjcfmgnpnvrsix1shncrlmone5zjvcdrv
3mc9qgkplqcqjdtwogmsxvcdhxccxtwortdpsjpx
8znfpbqv53seveneight
vpptlbbmqnfivekq7
one27ctq193onesix
66
znvvmjktwoblr8
tdqzhmsv4onefour
hqxdgtrhmxonetmpjmd3ltwo
rlppvdsrxpnxh6fivezdbbvgpbpqkxxvnnq2
37ninegthrzpzkrnine
lbtcrcmkckfmheight5ztvqpbt4
six7eight498two
1msqsmdfdpq6ninepxnjjfnmfivecfxhdrndbd4
8eight9four2
cpmeightwo5
seveneight2three6two
sevenonetwo2rqhkvnjthjmrdkhrbjsstfour
fksvone9four
snqbjfjmcbqpmonestj7bxgj
mhbxccsseveneight9gdzdkeightpk
mgks1seventtbnqcdllnine65qkfdrzm
83xzcd2ncvxdbgdrdklnmps4fxcndtkjsg
fsqgljbpxninesixfive55six1
34fqqseven2
3eight6nffcnjrsixsevenqf
dplzrgtn8xjnqpnxts1ninesqfhrdxrmn
szd83hxlnshsevenone3threetwo
csevenqnpmqhtpeight8twonelp
dxzfhlrpzzfive63dz4sevenrlqcxhjddv
xbgf81bxlthreepkjh53
8fourbbcnn
3gdthtqzjleight9sfmmzcone
ckrkgrxd88
three4zlkvrrmsgc28nineseven9
nine5hcp9
821pbsfmp388
two8eight2four8
14nine
four6vxpvfhfggnninesevenseven7twoone
3onethreemsjjvc7jblmdxrz
6gvfeightnineplmmbtsqxcxs
5four36ninemtpqtzpktqfpfive
zmxrctmxnfchrmsdxj1rbxkblsevenfourlgdppzfblh
7sixhqlrfqzzbppzzsssixlhtv
1teighteightdj
7cldkzgbn
mjsdlsgtwo2two
jbnfqjdl8
fourninesmff5fzsvpxvc
five3dzgrsrbsmc7pnlz
bbzch5twosixseven8one4
2229
six824881
onevtsjztc3twoeight1
72sixsgzpbpdjvtnxfivesixsix
1fournine
841five
qvrrpmdmgqseven1sthree
mkxbqcrxtsevendsrgvfkrgeightxrvfcgtwopsjnngn8
8dvjhfhhzbthree5p36
qqmhvjjnznxr95kkl9
9sixsevenz87
threejvpsvdxkgfg5three6bqmg5eight
f7four8eight5foursix6
8sstmfkpsjmxmrdkm3fpxxnpqmdhvrbkvgxxzfourseven
8vtpvlbkgxngcrjrsone8
jtwonexsgmlztnhtrljtfggkm5
cbtxjqqdqc56fourjhgtrjsxnbxnineeightwov
76zts8
fivehqftq3
5fiveqpncbfrrnp5sixfive
sevenseven9
8nine2fourdxxdghpmvseveneightwop
five4lzmvkqonefourtfhp
928
fourklbbjnr6
3eightdvpsbkf79klxnkkfour
67three
2two67hhsrfbdfournine3
lxpl2
sixsixjrkhthreeznvqgseven9kjlhc
34llhlctkks
rsgmz7nine3
3tdxfrvpktwofourfivevxtlllqvggft
seven2ninegcfrhbjxhlcntxzvp
321dcmcqmmfvfzvgmjp1mone
two12qlpxjdjqfc54seven2
eight5fjmsgjztwo
twotkdjqqbtt6twoone79sjkf
19one4
xvjtmnq15
sqvtzflq8onetwo3fghrstrd5three
4seven8rlrggvgtx9crnbseven8
59cxtwo55596
dkkdlsmmttwofour8
9xzvnnnr7jjjsrrxlsvggqplrqfpgl6rgrqgrqhr
kkbjcptltjsdjrlhzzg4drkffivezkxl
krsevenrcdq43
72fiverxszpfkgxtdjnspxmrt176
one5rjglslglzlhnhqj9
18bxgghx4
4fivegtxkxvqlskpv726foursqeightwonq
eightoneninetpht39two
four5982xjmvzxbhkqfive
sevenptlmncl4
4twonine3
nfpvhninefthreetwonine88
onervzkpxbrmnsbg3rkmjsfbltwo
gv2
eight5dhsprsgr
8qlbfive1flxrb8xcsfkdkxskdmk
gzv65rmkncqcveightfgfvfcmttkgvbxjg
two2pbxckhdlxfivetdqthree
84lgmvhxpldeight
jtjkmlfbmseven65xrnfbkn
9five2plxh2
6nineone5rgrkdzhsxj5
vjdfhvklsp2one9
sxfvgxgh4drmrhmbqjxhkr8jqnhqrnine
eightfivetp6mndcjqbdvzsix
seven7vt1
five65twotwo8eightjm2
mvvsix8threecl1clftjvjlgk
2threefivethree3rqhhdvxqmg8
qkkpvjfmpjcsmldtnine4nine
zgrpvl3
mdjnine1kjfkqqn
7mptczpscnq4vdfbveightfourjkhnhlkrkgch
pnineonetwo2
hkvtvvhrsrsevenfourone7kglfnjzztc
594eightpp1vseven
9bbghfmvgcpchvbfivesevenfoursix2
2three2796
sevenmzskghzgnxhqcq48htpczbhgvtwo
61hnccftjftjbnntsjhbfvvdtmlpbnnh3four
ljg79gdvhxdkmsqmsgnz
4ninebjgqqz
bszxzt4gone6n2
l4ctzkxbz
5qrhonetflqdnsztwonine9vnctxjnine
one5xrl2ldcrs
4eightnineone
zjlgvvpzpone9
1eight5three
vmvpknmkds9onegjxsfppqtwo7prv
threembbkvhlv28ktfjpd29
onefivehjvhjjbjj5jmqcmbxskninexkftfk
2eightjvpxjfzhcj
59glcksjlr6onefourtvszlbcztlbcjnkqn
sixxls6seventhreefdrhsfchfrfiveggdbmfqvxk
sixtwo62eightkcnrkmt
eightfivedpscseven93
191dhfpcjbn
rjhgbzqftwo247vhtnxone4gjrj
8fourctzsbsnine6sixfive4
four1dcczj
fourqnskksgg37sixeightpktnqvlm
7one26eightsix
six7sevenjbhfsshdtbvpbpzx
6jstxqcffive58twonelhf
2sixhcdkrprbskfpbb29lsxgpf
2qjlcphonefxx44six
ninecsssqzhone6nrmlkdhvthreefour
hrbnfive19
sevenfrtrbdqfournineeight2
mbkljfive5snsdsthmcdqrhpklxgx
43vvtqb5rfivesixkbxdkfgshjk
kgoneightqqxlrhtpx58threethree7vvqq
plqv7fivetwornc
six8bhgnfctwo
2ninejjtvxrffjfivesixtwo
mpntlbqvninepfkdgdrmrpxgs441
brcspjtbttnine16xhjhvzgf8fourrbdljsz
three1onefive
five1q59
2rxtthree3three
dd126gpdnjjgxmg9
eightone4cnpqrrdvvsixtfdfnlpmz
llrfourtwofourvlg78
ninehjhpnjbzdgxxcthree5
94vp4ftkxfh1
6tfrbtvdk5fivefive9zpgvfkfoureightwockn
bfnxmkjsevenfive8
9gqrnnmjddmz
four72snjxrhn
3three4eight339
four5fivervnxbscxjdtwolvnine
eight4xvsszglslfivetwosixsixfivekndrmh
ninesixeight6eight2seven1four
661seventwo
23dtscfgln7
6sixlcdqqx196
ftggvxqqlbrpkg629hxgsdnzxsrd7
3pmsbddckfivefkhxlhp7cmxgnf2
ghzqnkch7cjrs
four22
mpmzbnfour852r4six
r8one8five
onesix8threevxgpq17four
qnqeightwofcdsxgscgclpptnp9four1sixnjlvxqxxsnine
22ghnftqtmxzgfllzqkjvglrncgtwo
9twolkqtdzlg2qglgtnls
one3fivevhp4tpvjxccrnl
4jghljvxq
6n
5sevensevenzsxtrvprbrpmnzjnft8dtczjfgrcjqdtt
692rchkx
32gpqjfnsevenrnqcd
3fivejrgfjthreetwo869
sjtj4ninesix
9pqxqhfourthreeltjvpv3
twozxpthreenine931threethree
9kdmxssdm6fivesix5
3chmjhtwo67eightfour9
sixjt76fiveninedjzpceight3
6p36onern5
963seven
pgzrdxlqcb6ninejmxreight45seven
sevenmbgqvnnine5eight
twotwo5
hzbfour63nttfktqjzjhponeightcz
tnmbxcgrxbfivefive8cttmdeight
tklnv52two626htjghrccmzct
4nine7mninetwo
cfglfqttjrtnzrrb3jclcngt4
ftwo6eightgctgjzbrxlftlhvzc
kjscrvjhbtv7twoneq
four51onezkhllzssix1five
sprftsonesevenn3rmfive
m35five2fn
dcvvxzbmseven16
tlrone45
nrtfqlsxxvvcqtnjxzzonefour6329
bq64six
btwone79mkcmhlmfg
four35one
seveneightthreennbhgbsix6nine
8llbpdqqsbb
sevensvhzkjfxrnvxkp247five
qftsrhn3vsnbkpptqdsxdz
fjrp3threetwo7cbjsbrq
qzbbpk65
nttgvr42fzkr3sjgsfspnmfive
zsjnbntmmlqs7cgbdxcmqone9
threehpjbgphfqj2
onezjcmlcjmkfive7
fourthreefive86twosix
vlgfd31seven
flbqdkfqmj5htrzfpdjxeightsix
psh5eighteight8six
crzpzxt3eightvgfive466fbs
7cxxnglphqcxxnlbj635
threetwo6brzqxrbfrbffzllth3
jhcpvv8xccdmczvthree
fivehzsdct9ffmknlgtdmfzdfvmxvpj
68eight14zthree22
4qfdnl
seventnfnjtdv5qsrmksixffcrs7nine
1two5one
ninefmjlzkninethree3
hkkltwoone6hhkdkqdvznmnine7
rns2jmbcvp2
7tworgz5mxxtbjvg
twodxzfvhkzbtwo2qght
1bvl3
scxhtbssnghvkkhjr6v8
dxrztssg5jtdsix
4dhpvzsmxhbsixjrtqxmmcnkhv
2bxzpmzteightpshgffpn
onetwo14sevenlvvhls5sscsrpmzhsix
fourtwomxscgh6four
7mnzfive
xhzsgtppxgchc9threenine32fourthree
9nine4sevenqnhhglgfdccheight
mssoneight8three79vgpjxgjqseven7spgzdfbltl9
6zxkgeight
7mjqteightthreeeightdrnkjzzlm531
oneoneeighthhgsvj45dvzdvqxqkz
threedxsmlfqhpcs75eightthreecfbsgbfdxz
68two
48tjbzmqrpmjfpv
eightnine3six4pr6fmtfhxssrd
3rngpqfourtwonehqk
eighteightfour8tkgfkjcsixone5
7one3mcffpztdmzshrs2threecjmlsv
three1jznfive6dxlcxn
htzfvd1twoonesdrhpn
twofive7
five35ninephsixtwo
ninethreethreetwoninesevenfive8
3j4fivekcqj7
hzf9
7threefourseven6onenine
tkzdhq39fourfive34qkhh
one1mhhrglhvsbbqvj
ninebthreethree9four5stfspnine
hkmzxzhvfsevensix9three2seven
71six35threeqdhxbxrhcx9
clnzgbxkglf31
sixmsvpqdonetwo4fourpjrkmnpfdvvrfh
sixthree4one75
seven5eightsxnkzfbcnlpfhsixfive
98st
one7fivetwogvjpmx
gpvtdsix5
five9twotwo94qsxlslxq
78znzv8vbkqxnxhj3
3threeqfbxplhqxsr61
sevenjsvdxcjqjp5
hbjcnqqtd1twotwofive5two
vqdf19
52two47mkrnvrkpfivelvmgzjgcv
8nineone
ftqtbqqrqrsnnbnineninetwo6onenmjhvlr
onensgkpknpqxm3four3576
sixtndjcvprxzngkfivesixpvtft5
vtvkrnjvgninesktdqlzpt5
9kdfqnsmzz
6fourjbdqj
fivedmdphcz12ppltqpb82hdjldslp
ksqkttvninesevensix4pbnjsfznch5dlxfq
67hpqgstjlzsfive77
8vxrtgxfbk
6qksbmnineninekbzcbrmtjthree
76prtggdthree5seven
qksgrmmnvone1thmhh3twoeightsix
two2oneseven
cc9241nineninesixtwoneggs
fivesevenhqvrrqrhqlvnslvvqnzrnninebcmsmc3
nineeightsix42
vreightfourninefivep1
onedzn7mhvpnjsdgtzcp
fbvtnineone5five7
6oneninesixjgggcfkkltwo944
gcxkmnnbeightsix4
6one2eight6gbm33
threefivetwoxsrt7
5glzddtwo
94hmjcsevenfour2frqljgdrdfoureight
jqsfrllonedqvmm3n4six
913ninetwomkhvvfntng7seven
fournine8
fnmsx4jckrgtwoeightfour5pdhbb
8eighthrs
threethree4
nineqhkxhfslfrhfivep64sevensfg
three9nineseven7four4twooneightqbs
143seventlnvcdjt
clgltnktwohzmvrdcspfjc1twoqs
2five4
klt1xqmp5vkrpz
vdntdrrnz8vtxx
51sevengrvvqvnrmmsevenkqqnninefourskgxncnl
3cbcn
four5fivenine68three1
seventhree2sixls
4eight8sdprgt697seven
ptfdbpr414
9jrgnxqfourbmcl
1three8dseven9jfive
66pdxzvnzrqnkmfthreeqgnkdqvvcbcjbdsnz
threercbhjnckc8slv5ksrhvtt9fh8
six35tpf
pzrghq2four42
k8ninegqdcbnhb7mskvft25
2cxvggrthreedpplnjvsqhgfpbfivesixnpcsjn
ftwonethreefour9fivenine1five7
sixsixccfbbvxkrcnine71
9gcglxmjknhtwotwoone2onenineseven
khvppgl8eight
bzninebqfhn57
oneqbltgqlbpqdxgqonem4threefour1
xchkvlprvfgd59jdbfgvlbeight
84cjhvqmgdfh1fivesevenf
2one2
hxqfsjtwofivehbvndtpsevenseven44hkdstdkzs
nine4k1five
78rqrtjzsdfc3nine8twosqzzgsktmkcszzx
sixsix8
qkqhcfdckxsix29hfnnineg
twotgpfcdfcdtwocrffone5xcgtscjbmf
sevenfivenjvtctlkkmgeight9rxtjlnb8
ntqfzccxhjfourfmlgkheightmkplt5
1lpgdxeightqrmkqlxvcnntbvgzthree68
6four9two
threej5oneeight
pmlgczzpthreethree89btlvhfzbjd
8fiveeight
tvdkgbgrhplq66fldd
jsfkf54nvqmbnjmxks
gtpxlmphhgbgksixtwo9three
5ktgh
ggvzvfzmmmvrsqghrbd3kninezrlftwonebms
4two3z
fourzdfstskxhggkrl6eightndbxjeight8
3zdzlreight1827four4
2qlgkrbmnsgvmpninevjglsevenzdtmrqrnljthree
four2eightfiveldxtfjltseven6fourbddptkvjl
brrmvbfqkfczz7hthree
12fbdbbsrzss6dsrsrkjfhsrjxpxhvkfive
889srrl6six186
46tscxgjrxtwo4hlm35tzfxhrzsfd
fivesevenqgqzpcqnjdjlmg21hgnrdhfrp
2sixznfour6two
four4ztsfhvvmdkghh9one4
bdnmcghlkjmthree1sjhqbmmjtvfcxzleight9
bbqpd77jhlqbdp3fvnsevenfzxq
six7sixbd
8rstj9onetwonem
6one1
nineqstcshn35five
eightxndstksjj9xvmkhxgkqtwo4
fivek5xhqzvtplmczd35
zjsjmxmxeightp24fiveeight
9sjkjsjqxfnsdgxzmhjzfmbbmj
92qsbrtfour2onefourone
pkgc7sevenl9seven
glrkpdfhzddqvbceightpfxdgzm1eight
39bmsixjbzpkh72lklvgk
5four7onesevennfglmg
two6jvdmxqsthreeprfhq5
moneighthkdcpfhfmx8s9
twodkcs23fhj5
fourkcjdhmzvdbrkgj3onefive
mbmjrqlqzml21
threexmlgkxxms4rdrlcmlvx77
3mkjlxlkknfour
3four9
65ffd91
vxnxs8eightpl2three1mgdcrmfive
lnjkchzljjbznbdtxtgfnsevenone2ztxvtfzlbtwo
8eightoneightjb
qxxndbsfxpcmxdfrmzfkdvfvjplq6onetwo
36gjbxrllone4
rvljbxpglgpvxgq72
35ct69hzsgsb
six6sixzgxsfdkjtwo2drtbnine
ggdvhnngklthreezfqbzzbninephdhcgzvnine7csbq
54twofive19five4
bjeight4four
52mfcnnrhblfiveoneonelmdzg
ninebsj2lfx4gfsqrfsglx2eight9
3859csvhpkkksgpqnx22six
2onehdhqsndjrgspctkgjlnine7shxpd8hmlvdvsvqf
four5five6hkchns
fivetwofourgvthree9zxtrxf
onettmrcxbgfdpj99sixsix
onelqdmkfvxg4fourgvcqbtgqs
onehgrsfivedslxgxd19
eightxjf12sevenlsmglqrzrtpm4
vgppbqnskvpfivefivetqxlkbp3two
pkeightwopkz8rgtqhrhrjdmht3mz5
bbghbl9eightxcmftpndfive
oneseven2nxrcseven
fourthreefour5
53zsvpqnrjtwo5nine5nrdvmg
eight78twoone
bc6nf4zgnmkbnjts
xeightwopbgt7two
hqsnjjlbfivetwo84threepnine
br7oneeight2
ckxbsdjjttbxczfdpzmrxfh32eight
5212j912
1qhtwo3three9eight2nnjpbl
kdxx5five2ninebrvfzbbxptsccvdjgp
sixfpslbrfmqfvjs8seven
45qbcvqcjk6ninesix
98nine8
2eightonekcfvzfonethreenpxdpqtnvj
two87
jqnzhnzsdgg3eightfournbgsdxbfg31xrnv
4three3sxvnnzqvhcxj9
mpjmgpmninekffbkgprkb9tzzdznine8rtq
xhpfptdmpkeightdkqvpzscx7jndgsxxtqh
17vvktdvdgpthreeone1gqnb
fzpbhtmdvseven2one
sixzkkbjmnxnxm3gcvpsddqqgzktp63h
nineonexkqkfszg8qdzrlqszpltwo9cseven
7xfhtdfdldzplmrfivegpkgfseventwo
xvone5two7
fiveqdrgeightvrvtmtvvmnl2kbctwofive
three9rrxhddsdfive577
mnkltgsgs4fivefivekxzzhjdtnzzvmvxdh
blqtmklmkxcjtmxsrflffpzjcrninecd7rgdn8
jgpktmfourdxzll8threerlssqvslnb
4grvtbmlpqxgmzzksfgzvjggsqhffq1qcd
cninebtfvxfnmbtznfnzdh4zdmgtvbbnine
1seven4vkvqcktfourvjtd4zqh
8eight7lhmx89four
xrpxkdrf8fhl29fivexzsrdbmksixpvlk
8tvfplhxxxzr
twothree8nine2ninegfbrchxmmfive
9threeskhgsnsvvzpnnv2seven4
8sbzvncqszzdflznpqfddeight3
1eightzfivehlmhnqbnnr
sixfivefjfqftjvcdzkpbkhnvqrqqhpvmgnq75pfk
mtfvjbbpdeight1
txtfqxvbrnine2
sevenptvlbpkdzpp8tnlvkdjjpbt
qgoneighteighttgrdmljtzbblrtskvfivevbbp1
ninethreejbxseven392
86pbrnhhhpn
sevenonenine5bcqrttts6fourthree
4seventwo5ngnbkqftzdfive4lhsthree
36seven97klhbqbpgninerb
813eight
ncbfctqlsnfive1brqpthree4
ksbsddjcknsevensix293three
rljzzbvd3zkmbpjt9eightninesnlrsone
97ninesevenrhchvppnztvfbfpkzrbcone
sevendxbninefour2fourclmln
1rdtwofjvdllht5eightsixfourbl"""

def find_first(string):
    index = 100 

    if "one" in string:
        if index > string.index("one"):
            index = string.index("one")
        
    if "two" in string:
        if index > string.index("two"):
            index = string.index("two")
    if "three" in string:
        if index > string.index("three"):
            index = string.index("three")
    if "four" in string:
        if index > string.index("four"):
            index = string.index("four")
    if "five" in string:
        if index > string.index("five"):
            index = string.index("five")
    if "six" in string:
        if index > string.index("six"):
            index = string.index("six")
    if "seven" in string:
        if index > string.index("seven"):
            index = string.index("seven")
    if "eight" in string:
        if index > string.index("eight"):
            index = string.index("eight")
    if "nine" in string:
        if index > string.index("nine"):
            index = string.index("nine")
    if "zero" in string:
        if index > string.index("zero"):
            index = string.index("zero")
    

    if "one" in string[index:index+4]:
        return 1, index
    if "two" in string[index:index+4]:
        return 2, index
    if "three" in string[index:index+6]:
        return 3, index
    if "four" in string[index:index+5]:
        return 4, index
    if "five" in string[index:index+5]:
        return 5, index
    if "six" in string[index:index+4]:
        return 6, index
    if "seven" in string[index:index+6]:
        return 7, index
    if "eight" in string[index:index+6]:
        return 8, index
    if "nine" in string[index:index+5]:
        return 9, index
    if "zero" in string[index:index+5]:
        return 0, index
    
    return 1000,1000



def find_last(string):
    index = 100 
    if "eno" in string:
        if index > string.index("eno"):
            index = string.index("eno")
        
    if "owt" in string:
        if index > string.index("owt"):
            index = string.index("owt")
    if "eerht" in string:
        if index > string.index("eerht"):
            index = string.index("eerht")
    if "ruof" in string:
        if index > string.index("ruof"):
            index = string.index("ruof")
    if "evif" in string:
        if index > string.index("evif"):
            index = string.index("evif")
    if "xis" in string:
        if index > string.index("xis"):
            index = string.index("xis")
    if "neves" in string:
        if index > string.index("neves"):
            index = string.index("neves")
    if "thgie" in string:
        if index > string.index("thgie"):
            index = string.index("thgie")
    if "enin" in string:
        if index > string.index("enin"):
            index = string.index("enin")
    if "orez" in string:
        if index > string.index("orez"):
            index = string.index("orez")
    

    if "eno" in string[index:index+4]:
        return 1, index
    if "owt" in string[index:index+4]:
        return 2, index
    if "eerht" in string[index:index+6]:
        return 3, index
    if "ruof" in string[index:index+5]:
        return 4, index
    if "evif" in string[index:index+5]:
        return 5, index
    if "xis" in string[index:index+4]:
        return 6, index
    if "neves" in string[index:index+6]:
        return 7, index
    if "thgie" in string[index:index+6]:
        return 8, index
    if "enin" in string[index:index+5]:
        return 9, index
    if "orez" in string[index:index+5]:
        return 0, index
    
    return 1000,1000


splitted_string = input_string.split("\n")

print(len(splitted_string))


nums  = []
for each in splitted_string:
    firstnum=""
    lastnum =""
    
    for subeach in each:
        if subeach.isdigit():
            firstnum = subeach
            break
    fnum,i = find_first(each)
    if firstnum=="" or each.index(firstnum) > i:
        firstnum = str(fnum)


    for subeach in each[::-1]:
        if subeach.isdigit():
            lastnum = subeach
            break
    lnum,i = find_last(each[::-1])
    if lastnum=="" or each[::-1].index(lastnum) > i:
        lastnum = str(lnum)
    
    nums.append(int(firstnum+lastnum))


print(nums)
print(len(nums))

print("sum", sum(nums))