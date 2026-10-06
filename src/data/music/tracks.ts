export type MusicTrackKind = "theme" | "stage" | "boss" | "character-boss";

export interface MusicTrackVersion {
  label?: string;
  duration: string;
  audioPath?: string;
  lyrics?: string;
}

export interface MusicTrack {
  id: string;
  title: string;
  titleEn: string;
  kind: MusicTrackKind;
  kindLabel: string;
  day?: number | string;
  character?: string;
  cover: string;
  coverPlaceholder?: boolean;
  titleSeparator?: "~" | "～";
  description: string;
  versions: MusicTrackVersion[];
}

export const musicTracks: MusicTrack[] = [
  {
    id: "lets-go-see",
    title: "先去看看吧",
    titleEn: "Let’s Go See",
    kind: "theme",
    kindLabel: "主题曲",
    cover: "media/promotion/p02-seven-days.png",
    coverPlaceholder: true,
    description: "《東方七日祭》的正式主题曲。故事从灵梦那句随口的“先去看看吧”开始；Piano Version 则把同一旋律收得更安静。",
    versions: [
      {
        label: "Original",
        duration: "4:08",
        audioPath: "media/music/previews/lets-go-see.mp3",
        lyrics: "[Intro]\n风起了\n天亮了\n今天啊\n好像和平常\n有一点不一样\n去看看吧\n\n[Verse 1]\n风还在\n路还长\n\n[Verse 1]\n风还在\n路还长\n那就\n再走一点吧\n山下面有人说笑\n山上又有人来\n不知道从什么时候起\n今天比昨天热闹一些\n有人赶路\n有人停下来\n有人说每年都是这样\n我想了半天\n也没想出哪里奇怪\n\n[Refrain]\n那就再往前走吧\n反正太阳还没落下\n从神社走到山里\n从白天走到灯亮\n今天没问明白的事\n明天也可以再问啊\n七天才刚刚开始\n不用这么早回家\n\n[Interlude]\n\n[Verse 2]\n风停了\n又吹来\n路边的声音\n少了一点\n熟悉的人还是熟悉\n只是话比平时多\n昨天经过的那条路\n今天又换了一种走法\n有人记得\n有人忘了\n有人觉得没有什么\n可走得久了\n总觉得哪里少了一点\n\n[Refrain]\n那就再往前走吧\n那就再往前走吧\n看看下一盏灯在哪\n从山路走到夜里\n从人群走到安静\n今天没问明白的事\n明天也许会想起来\n七天还没有走完\n不用急着说为什么\n\n[Bridge]\n如果明天还是这样\n那就明天再看看\n如果后天还是这样\n后天再走远一点\n路总会有尽头\n风也总会停一下\n风也总会停一下\n可现在\n天还没有黑透\n所以——\n再走一会儿吧\n\n[Final Refrain]\n风又起了\n天又亮了\n今天啊\n好像和平常\n也没有那么不一样\n可走过这些路以后\n总会记住一些什么吧\n七天终于走到这里\n明天也还是明天\n\n[Outro]\n嘛——\n总之\n先去看看吧\n\n[Outro]\n嘛——\n总之\n先去看看吧",
      },
      {
        label: "Piano Version",
        duration: "3:28",
        audioPath: "media/music/previews/lets-go-see-piano.mp3",
      },
    ],
  },
  {
    id: "holiday-road",
    title: "闲人满山路",
    titleEn: "Holiday Road",
    kind: "stage",
    kindLabel: "道中曲",
    day: 1,
    cover: "media/promotion/p02-seven-days.png",
    coverPlaceholder: true,
    description: "第一日的山路曲。人比平时多，路却还是那条路；灵梦就这样一路看过去。",
    versions: [
      {
        duration: "2:59",
        audioPath: "media/music/previews/holiday-road.mp3",
      },
    ],
  },
  {
    id: "no-through-road",
    title: "此路不通",
    titleEn: "No Through Road",
    kind: "boss",
    kindLabel: "Boss 曲",
    day: 1,
    cover: "media/promotion/p02-seven-days.png",
    coverPlaceholder: true,
    description: "第一日的 Boss 曲。路走到这里，终于有人很认真地说：不许再往前。",
    versions: [
      {
        duration: "2:25",
        audioPath: "media/music/previews/no-through-road.mp3",
      },
    ],
  },
  {
    id: "echoes-of-shishi",
    title: "檐下三响",
    titleEn: "Echoes of Shishi",
    kind: "character-boss",
    kindLabel: "Boss 曲",
    day: "6 → 7",
    character: "沈诗诗",
    cover: "media/music/covers/echoes-of-shishi.png",
    titleSeparator: "~",
    description: "沈诗诗的核心角色同人曲，同时也是她的 Final Boss Theme。战斗从第六日深夜跨到第七日清晨；纯音乐版保留游戏感，Vocal Version 则把诗诗与檐下回声写得更完整。",
    versions: [
      {
        label: "Instrumental",
        duration: "3:24",
        audioPath: "media/music/previews/echoes-of-shishi.mp3",
      },
      {
        label: "Vocal Version",
        duration: "3:25",
        audioPath: "media/music/previews/echoes-of-shishi-vocal.mp3",
        lyrics: "【Intro】\n谁的影子\n落在旧檐上？\n小灯晃呀晃\n风也跟着晃\n我才走过半边回廊\n怎么——\n又有一声响？\n\n【Verse 1】\n窗纸亮一点\n月色凉一点\n鞋尖踩过青石边\n门呀别乱推\n东西别乱翻\n我刚刚不是说过一遍？\n东厢静悄悄\n西厢也静悄悄\n只有你的脚步\n跑得有一点吵\n喂——\n你到底在找什么呀？\n\n【Pre-Chorus】\n一声落在檐角\n一声绕过回廊\n方才走远的声音\n怎么又回到身旁\n我停下来听呀听\n灯影轻轻晃呀晃\n梆——\n梆——\n梆——\n……还在那里呀？\n\n【Chorus】\n梆、梆、梆——\n谁在响？\n檐下一声\n绕过回廊\n灯一晃\n袖一扬\n小小的影子\n站在月光上\n你往东——\n它往东\n你往西——\n它往西\n你留下的每一声\n都、会、回、来——\n所以呀——\n别再乱跑啦！\n\n【Verse 2】\n明明说好了\n那边不能去\n怎么一转身你又过去？\n\n【Verse 1】\n柜门轻轻响\n窗边风一挤\n窗边风一挤\n连桌上的灯都跟着急\n我没有生气……\n真的没有生气。\n只是你再往前一步——\n我、我可要认真啦！\n\n【Pre-Chorus 2】\n一声藏进瓦上\n一声落进庭旁\n一声追着你的脚步\n越走越长\n旧门应一声\n窗棂应一声\n连我刚说过的话\n也在后面跟\n“别过去呀——”\n……过去呀……\n“都说过啦——”\n……说过啦……\n\n【Chorus 2】\n梆、梆、梆——\n又在响！\n满院回声\n一起登场\n灯一晃\n夜一亮\n小小的影子\n站在月中央\n你进一步——\n它进一步\n你若转身——\n它也转身\n你留下的每一声\n都、别、想、跑——\n这一次——\n可不能装作没听到！\n\n【Bridge】\n月过檐牙\n风过窗纱\n旧屋静静睡着啦\n只有一盏灯\n还没有回家\n梆。\n一声问——\n“是谁呀？”\n梆。\n一声答——\n“是你呀。”\n梆。\n再一声——\n从很远很远的地方\n轻轻回来啦。\n听见吗？\n这一声绕过\n长长回廊\n灯影摇\n衣角扬\n小小的身影\n还站在月光上\n一声落下——\n百声回答\n窗也回答\n门也回答\n你留下的每一声\n都、会、回、家——\n你看呀——\n我早就说过啦。\n这里的声音\n一个也不会走丢呀。\n\n【Outro】\n小灯晃呀晃。\n谁的影子\n走过旧檐下？\n……好啦。\n这次真的\n不许再乱翻啦。",
      },
    ],
  },
];
