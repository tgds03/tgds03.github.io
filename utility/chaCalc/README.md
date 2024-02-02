# 이게 뭔가요

야마하 사의 VOCALOID 엔진에서 CHA, PB 파라미터에 따라 형성되는 스펙트럼을 보여주는 프로그램입니다. 

도식에서 빨간 선으로 표시되는 배음열이 스펙트럼에서 그려지는 부분입니다. 정확하진 않으니 참고용으로 사용해주세요.

# 매뉴얼

![](/media/스크린샷%202024-02-02%20145201.png)

상단 탭에서 라이브러리를 선택할 수 있습니다. 지금은 한국어 라이브러리에 대해서만 제공됩니다.

하단에서 모음 선택, 파라미터 조정을 할 수 있습니다. 

- **모음**: 라이브러리에서 사용 가능한 모음을 선택할 수 있습니다. 단모음만 가능합니다.
- **노트**: 노트를 선택합니다. C2 ~ C6 [^1] 내에서 선택할 수 있습니다.
- **CHA**: VOCALOID 엔진 내 파라미터인 CHA에 대응됩니다.
- **PB**: VOCALOID 엔진 내 파라미터인 PB에 대응됩니다. 파라미터 범위인 -8192 ~ 8191을 벗어나면 노란색으로 표시됩니다.
  - PB 값과 함께 PB에 대응되는 음정 값이 cent로 계산됩니다.
  - PB 값을 결정하는 파라미터인 PBS를 오른쪽에서 선택할 수 있습니다.
- **Pitch**: 노트와 PB를 통해 계산한 음높이입니다. [^1]
- **Pitch Lock**: Pitch를 고정시킵니다. 활성화 시 노트, PB가 Pitch에 맞춰 조정됩니다.

[^1]: 국제표기(440hz=A4)가 아닌 야마하의 표기(440hz=A3)를 따릅니다. 

중간의 스펙트럼 도식에서 선택한 모음, 파라미터에 따라 그려질 스펙트럼을 보여줍니다.

- **스펙트럼 도식**: 스펙트럼을 보여줍니다. x축은 Hz단위 ( ~ 5kHz), y축은 dB 단위(0dB ~ -100dB)입니다.
- **모음 필터**: 모음을 결정하는 가상의 필터입니다.
  - 소스필터 이론의 필터에 대응됩니다. 즉, 성대 진동으로 발생한 음을 변형시키는 모델입니다.
  - 이 필터에서 두드러지게 높은 부분은 포먼트에 대응됩니다.
- **배음열**: 파라미터를 통해 만들어진 음원의 주파수 특성입니다. 스펙트럼에 실제로 그려지는 부분입니다.