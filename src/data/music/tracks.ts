export type MusicTrackKind = "theme" | "stage" | "boss" | "character-boss";

export interface MusicTrackVersion {
  label?: string;
  duration: string;
  audioPath?: string;
}

export interface MusicTrack {
  id: string;
  title: string;
  titleEn: string;
  kind: MusicTrackKind;
  kindLabel: string;
  day?: number;
  character?: string;
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
    description: "《東方七日祭》的正式主题曲。故事从灵梦那句随口的“先去看看吧”开始；Piano Version 则把同一旋律收得更安静。",
    versions: [
      { label: "Original", duration: "4:08" },
      { label: "Piano Version", duration: "3:28" },
    ],
  },
  {
    id: "holiday-road",
    title: "闲人满山路",
    titleEn: "Holiday Road",
    kind: "stage",
    kindLabel: "道中曲",
    day: 1,
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
    kindLabel: "沈诗诗角色曲 / Boss Theme",
    character: "沈诗诗",
    description: "沈诗诗的核心角色同人曲，同时也是她的 Boss Theme。纯音乐版用于保留游戏感，Vocal Version 则把诗诗与檐下回声写得更完整。",
    versions: [
      { label: "Instrumental", duration: "3:24" },
      { label: "Vocal Version", duration: "3:25" },
    ],
  },
];
