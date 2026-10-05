export type MusicTrackKind = "theme" | "stage" | "boss" | "character-boss";

export interface MusicTrack {
  id: string;
  title: string;
  titleEn: string;
  kind: MusicTrackKind;
  kindLabel: string;
  day?: number;
  character?: string;
  description: string;
  audioPath?: string;
  duration?: string;
}

export const musicTracks: MusicTrack[] = [
  {
    id: "lets-go-see",
    title: "先去看看吧",
    titleEn: "Let’s Go See",
    kind: "theme",
    kindLabel: "主题曲",
    description: "《東方七日祭》的正式主题曲。故事从灵梦那句随口的“先去看看吧”开始，主旋律也会在游戏里的其他曲目中留下回声。",
  },
  {
    id: "holiday-road",
    title: "闲人满山路",
    titleEn: "Holiday Road",
    kind: "stage",
    kindLabel: "道中曲",
    day: 1,
    audioPath: "media/music/previews/holiday-road.mp3",
    duration: "2:59",
    description: "第一日的山路曲。人比平时多，路却还是那条路；灵梦就这样一路看过去。",
  },
  {
    id: "no-through-road",
    title: "此路不通",
    titleEn: "No Through Road",
    kind: "boss",
    kindLabel: "Boss 曲",
    day: 1,
    audioPath: "media/music/previews/no-through-road.mp3",
    duration: "2:25",
    description: "第一日的 Boss 曲。路走到这里，终于有人很认真地说：不许再往前。",
  },
  {
    id: "echoes-of-shishi",
    title: "檐下三响",
    titleEn: "Echoes of Shishi",
    kind: "character-boss",
    kindLabel: "沈诗诗角色曲 / Boss Theme",
    character: "沈诗诗",
    description: "沈诗诗的核心角色同人曲，同时也是她的 Boss Theme。它不是另一首独立的“诗诗 Boss 曲”；角色曲与战斗主题使用的是同一个音乐核心。",
  },
];
