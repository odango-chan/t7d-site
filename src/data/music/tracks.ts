export type MusicTrackKind = "stage" | "boss" | "character-boss";

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
    id: "holiday-road",
    title: "闲人满山路",
    titleEn: "Holiday Road",
    kind: "stage",
    kindLabel: "道中曲",
    day: 1,
    description: "第一日的山路曲。人比平时多，路却还是那条路；灵梦就这样一路看过去。",
  },
  {
    id: "no-through-road",
    title: "此路不通",
    titleEn: "No Through Road",
    kind: "boss",
    kindLabel: "Boss 曲",
    day: 1,
    description: "第一日的 Boss 曲。路走到这里，终于有人很认真地说：不许再往前。",
  },
  {
    id: "echoes-of-shishi",
    title: "檐下三响",
    titleEn: "Echoes of Shishi",
    kind: "character-boss",
    kindLabel: "诗诗 Boss 曲",
    character: "沈诗诗",
    description: "属于沈诗诗的 Boss 曲。和前面的山路不同，这一首更贴近她自己的气质与节奏。",
  },
];
