# Playlist

한국의 평범한 일상과 전통적인 정서를 현대적인 카페 음악으로 기록하는 플레이리스트 프로젝트입니다.

목표는 음악 이론을 잘 몰라도 AI 음악 생성 모델을 활용해, 카페나 작업 공간에서 오래 틀어두기 좋은 곡들을 꾸준히 만드는 것입니다.

## Concept

프로젝트 방향:

- 한국의 소소한 일상 장면을 가사와 사운드로 기록한다.
- 카페에서 대화를 방해하지 않는 부드러운 음악을 만든다.
- 전통 악기는 주인공이 아니라 질감으로 사용한다.
- 보컬곡과 instrumental 버전을 함께 만든다.
- 한 곡보다 하나의 일관된 플레이리스트/브랜드로 쌓아간다.

추천 프로젝트 이름 후보:

- 오늘의 풍경
- 창가의 일기
- 골목의 노래
- 작은 계절
- 오후 네 시
- 평범한 하루의 기록

## Recommended Direction

기본 사운드:

- soft felt piano
- warm acoustic guitar
- gentle lo-fi drums
- soft bass
- subtle gayageum texture
- light daegeum or haegeum phrases
- rain, wind, room tone, street ambience

피해야 할 방향:

- 너무 강한 EDM 국악 퓨전
- 보컬이 지나치게 전면에 나오는 편곡
- 카페 배경음악으로 쓰기 어려운 과한 드럼/브라스/고음
- 특정 기존 곡을 직접 모방하는 프롬프트

## Recommended AI Models

### 1. ACE-Step

가장 먼저 테스트할 모델입니다.

- 한국어 포함 다국어 가사 기반 생성 가능
- 보컬과 반주가 있는 곡 생성에 적합
- GUI가 있어 초보자에게 비교적 접근성이 좋음
- 라이선스가 비교적 실험과 배포에 유리한 편

Use case:

- 한국어 가사 카페곡
- 보컬 버전 생성
- 같은 곡의 instrumental 버전 생성

### 2. DiffRhythm

빠르게 여러 방향을 실험하는 용도에 좋습니다.

- 긴 곡 생성 실험
- instrumental BGM 생성
- 여러 장르 태그 비교

### 3. Stable Audio Open / Stable Audio 3 계열

보컬 없는 카페 BGM과 앰비언트 질감에 좋습니다.

- instrumental
- background music
- rain cafe
- hanok ambience

라이선스는 사용 범위에 따라 확인이 필요합니다.

### 4. YuE

더 긴 보컬곡과 풀송 제작을 실험할 때 사용합니다.

- 세팅 난이도는 높을 수 있음
- 가사 기반 풀송 생성에 적합

### 5. MusicGen / AudioCraft

학습과 참고 실험용으로 좋지만, 모델 라이선스가 비상업 제한일 수 있으므로 실제 배포 전 반드시 확인합니다.

## Project Structure

권장 폴더 구조:

```text
playlist/
  README.md
  docs/
    concept.md
    model-notes.md
    production-workflow.md
  prompts/
    ace-step/
    diffrhythm/
    stable-audio/
  lyrics/
    001-convenience-store-coffee.md
  tracks/
    001-convenience-store-coffee/
      brief.md
      prompt.md
      lyrics.md
      notes.md
  exports/
    # generated audio files, not committed by default
```

현재는 README부터 시작하고, 곡을 만들기 시작하면 위 구조로 확장합니다.

## How To Continue On Another Computer

1. 저장소를 클론합니다.

```bash
git clone https://github.com/visualog/playlist.git
cd playlist
```

2. 작업 브랜치를 만듭니다.

```bash
git checkout -b work/first-playlist
```

3. 사용할 모델을 하나 고릅니다.

초기 추천:

- 가사 있는 곡: ACE-Step
- 보컬 없는 카페 BGM: Stable Audio 계열 또는 DiffRhythm
- 긴 풀송 실험: YuE

4. 첫 곡 폴더를 만듭니다.

```bash
mkdir -p tracks/001-convenience-store-coffee
```

5. `brief.md`, `lyrics.md`, `prompt.md`, `notes.md`를 작성합니다.

6. 모델에서 여러 버전을 생성합니다.

7. 마음에 드는 버전을 고르고, 보컬 버전과 instrumental 버전을 따로 정리합니다.

8. 생성 파일이 큰 경우 GitHub에 직접 커밋하지 말고 Git LFS, Release, 외부 스토리지 중 하나를 사용합니다.

## First Playlist Roadmap

첫 플레이리스트는 10곡으로 시작합니다.

| No. | Title | Scene | Mood |
| --- | --- | --- | --- |
| 001 | 편의점 커피 | 아침 편의점 종이컵 커피 | 따뜻한 시작 |
| 002 | 오늘도 같은 버스 | 출근길 버스 정류장 | 담담하고 편안함 |
| 003 | 비 오는 횡단보도 | 장마철 오후 | 차분한 로파이 |
| 004 | 창가 자리 | 카페에서 바라본 거리 | 피아노 중심 |
| 005 | 골목 끝 불빛 | 저녁 골목길 | 잔잔한 기타 |
| 006 | 세탁기 돌아가는 소리 | 평범한 밤 | 생활감 있는 앰비언트 |
| 007 | 엘리베이터 12층 | 이웃과 짧은 인사 | 미니멀한 보컬곡 |
| 008 | 대나무 바람 | 한국적 자연감 | 대금 질감 |
| 009 | 퇴근길 노을 | 하루 마무리 | 따뜻한 스트링 |
| 010 | 오늘도 괜찮았어 | 별일 없는 하루 | 엔딩곡 |

## Song Brief Template

```text
Title:
Scene:
Time:
Weather:
Emotion:
Tempo:
Key:
Vocal:
Instruments:
Traditional Korean texture:
Avoid:
Reference mood:
```

Example:

```text
Title: 편의점 커피
Scene: 이른 아침, 골목 끝 편의점에서 종이컵 커피를 사는 순간
Time: 08:10
Weather: 맑지만 아직 서늘한 아침
Emotion: 별일 없지만 나쁘지 않은 하루
Tempo: 76-82 BPM
Key: G major or C major
Vocal: soft, intimate Korean vocal
Instruments: felt piano, acoustic guitar, soft bass, brush drums
Traditional Korean texture: subtle gayageum pluck in the background
Avoid: dramatic chorus, strong EDM drums, trot feeling, overly sad ballad
Reference mood: cozy Korean indie cafe playlist
```

## Prompt Template

Use this as a starting point for ACE-Step or another music generation model.

```text
A cozy modern Korean cafe song about ordinary daily life.
Soft felt piano, warm acoustic guitar, gentle lo-fi drums, soft bass, and subtle gayageum texture.
Calm intimate Korean vocal, not overpowering.
Mood: warm, nostalgic, peaceful, simple, not sad.
Tempo: 78 BPM.
Arrangement should be minimal and suitable for background music in a cafe.
Avoid dramatic climax, loud drums, EDM drop, and overly traditional fusion.
Create a repeatable playlist-friendly song with a soft intro, verse, small chorus, and gentle outro.
```

## Lyric Style

가사는 큰 사건보다 작은 장면을 씁니다.

좋은 소재:

- 버스를 기다리는 5분
- 편의점 커피
- 비 오는 횡단보도
- 창문으로 들어오는 바람
- 퇴근길 노을
- 빨래가 마르는 오후
- 이웃과 짧은 인사
- 오래된 골목의 불빛
- 카페 창가 자리
- 장마가 시작된 날

기본 톤:

- 일기처럼 담담하게
- 너무 시적이기보다 구체적으로
- 한국의 풍경은 직접 설명하지 말고 사물과 장소로 느껴지게

## First Lyric Draft

```text
제목: 편의점 커피

오늘도 같은 골목을 지나
불 켜진 편의점 앞에 서면
아직 덜 깬 아침 냄새와
종이컵 하나의 온기

별일은 없을 것 같은 하루
그래도 나쁘진 않을 것 같아
작은 숨을 한 번 고르고
문득 웃게 되는 아침
```

## Production Workflow

1. 일상 장면 하나를 고른다.
2. 4-8줄의 짧은 가사를 쓴다.
3. 곡 브리프를 작성한다.
4. AI 모델에 넣을 프롬프트를 만든다.
5. 4-8개의 버전을 생성한다.
6. 가장 자연스러운 버전 1-2개를 고른다.
7. 보컬 버전과 instrumental 버전을 따로 만든다.
8. 카페에서 10분 이상 들어보며 방해되는 요소를 체크한다.
9. 곡별 노트를 남긴다.
10. 최종 플레이리스트 순서를 정한다.

## Review Checklist

- 카페에서 대화에 방해되지 않는가?
- 3번 반복해서 들어도 피로하지 않은가?
- 보컬이 너무 앞에 있지 않은가?
- 전통 악기 느낌이 과하지 않은가?
- 제목과 장면이 실제 음악 분위기와 맞는가?
- instrumental 버전도 쓸 수 있는가?
- 라이선스와 모델 사용 조건을 확인했는가?

## Notes On Generated Audio

생성된 오디오 파일은 용량이 커질 수 있으므로 기본적으로 Git에 커밋하지 않습니다.

권장 방식:

- 작업용 음원: 로컬 `exports/` 폴더
- 공유용 음원: GitHub Release 또는 별도 스토리지
- 장기 보관: 원본 프롬프트, 가사, 모델명, seed, 생성 날짜를 함께 기록

## Next Tasks

- `docs/concept.md` 작성
- `tracks/001-convenience-store-coffee/` 생성
- 첫 곡용 `brief.md`, `lyrics.md`, `prompt.md` 작성
- ACE-Step 설치 및 첫 테스트 생성
- 보컬 버전과 instrumental 버전 비교
