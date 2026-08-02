---
type: smite-build
god: Loki
mode: Conquest
builds:
- source: community
  aspect: Aspect of Agony
  aspect_pick_rate: 0.32
  aspect_win_rate: 0.62
  slot_order:
  - name: Jotunn's Revenge
    pick_rate: 0.35
    win_rate: 0.6
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.23
      win_rate: 0.6
    - name: Hydra's Lament
      pick_rate: 0.12
      win_rate: 0.62
  - name: Hydra's Lament
    pick_rate: 0.28
    win_rate: 0.55
    alternates:
    - name: Jotunn's Revenge
      pick_rate: 0.14
      win_rate: 0.6
    - name: Transcendence
      pick_rate: 0.13
      win_rate: 0.56
  - name: Barbed Carver
    pick_rate: 0.16
    win_rate: 0.61
    alternates:
    - name: Hydra's Lament
      pick_rate: 0.18
      win_rate: 0.59
    - name: Genji's Guard
      pick_rate: 0.1
      win_rate: 0.61
  - name: Heartseeker
    pick_rate: 0.25
    win_rate: 0.57
    alternates:
    - name: Titan's Bane
      pick_rate: 0.15
      win_rate: 0.56
    - name: Dwarven Plate
      pick_rate: 0.06
      win_rate: 0.41
  - name: Titan's Bane
    pick_rate: 0.16
    win_rate: 0.53
    alternates:
    - name: Heartseeker
      pick_rate: 0.15
      win_rate: 0.62
    - name: The Crusher
      pick_rate: 0.05
      win_rate: 0.58
  - name: Blinking Abyss
    pick_rate: 0.08
    win_rate: 0.7
    alternates:
    - name: Skeggox
      pick_rate: 0.07
      win_rate: 0.56
    - name: Lucerne Hammer
      pick_rate: 0.07
      win_rate: 0.56
  source_url: https://smitebrain.com/gods/loki/
  last_verified: '2026-08-01'
  god_win_rate: 0.5772151898734177
  god_matches_won: 228
  god_matches_played: 395
  god_division: obsidian
  god_window_start: '2026-07-28'
  god_window_end: '2026-08-01'
  god_matches_analyzed: 4952
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - Runeforged Hammer
  - The Reaper
  - The Crusher
  - Heartseeker
  flex_slots:
  - The Reaper
  - Runeforged Hammer
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: The Crusher, The Reaper, Runeforged Hammer, Avatar''s Parashu, Lernaean
    Bow, Pendulum Blade, Tekko-Kagi, Avenging Blade, Damaru, Blink Rune, Arondight,
    Golden Blade, Shield Splitter, Eye of the Storm, Tyrfing, Genji''s Guard, Bloodforge,
    Riptalon, Transcendence, Berserker''s Shield, Wyrmskin Hide, Breastplate of Valor,
    Musashi''s Dual Swords, Oni Hunter''s Garb.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.68
      efficiency: 0.69
      win: 0.6
      pick: 0.35
      fit: 1.0
    Hydra's Lament:
      total: 0.61
      efficiency: 0.69
      win: 0.55
      pick: 0.28
      fit: 0.71
    Runeforged Hammer:
      total: 0.56
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.62
    The Reaper:
      total: 0.57
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.91
    The Crusher:
      total: 0.62
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 1.0
    Heartseeker:
      total: 0.6
      efficiency: 0.53
      win: 0.57
      pick: 0.25
      fit: 1.0
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: burst
  slot_order:
  - Blink Rune
  - Jotunn's Revenge
  - Hydra's Lament
  - Runeforged Hammer
  - The Crusher
  - Heartseeker
  flex_slots:
  - Blink Rune
  - Runeforged Hammer
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: The Crusher, Blink Rune, Runeforged Hammer, Genji''s Guard, The Reaper, Pendulum
    Blade, Avatar''s Parashu, Lernaean Bow, Arondight, Breastplate of Valor, Avenging
    Blade, Damaru, Riptalon, Tekko-Kagi, Berserker''s Shield, Golden Blade, Shield
    of the Phoenix, Oni Hunter''s Garb, Chandra''s Grace, Yogi''s Necklace, Freya''s
    Tears, Kinetic Cuirass, Amanita Charm, Shield Splitter, Eye of the Storm.'
  slot_scores:
    Blink Rune:
      total: 0.53
      efficiency: 0.87
      win: 0.5
      pick: 0.0
      fit: 0.0
    Jotunn's Revenge:
      total: 0.65
      efficiency: 0.69
      win: 0.6
      pick: 0.35
      fit: 0.78
    Hydra's Lament:
      total: 0.58
      efficiency: 0.69
      win: 0.55
      pick: 0.28
      fit: 0.54
    Runeforged Hammer:
      total: 0.52
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.32
    The Crusher:
      total: 0.57
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.66
    Heartseeker:
      total: 0.55
      efficiency: 0.53
      win: 0.57
      pick: 0.25
      fit: 0.66
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Hydra's Lament
  - Runeforged Hammer
  - Amanita Charm
  flex_slots:
  - Shield of the Phoenix
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Eye of Providence — magical protection
    swap_item: Eye of Providence
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Runeforged Hammer, Shield of the Phoenix, Kinetic Cuirass,
    The Crusher, Berserker''s Shield, The Reaper, Eye of Providence, Oni Hunter''s
    Garb, Blink Rune, Avenging Blade, Eye of the Storm, Chandra''s Grace, Spectral
    Armor, Shield Splitter, Genji''s Guard, Shifter''s Shield, Golden Blade, Phoenix
    Feather, Riptalon, Pharaoh''s Curse, Erosion, Draconic Scale, Yogi''s Necklace,
    Lernaean Bow, Mantle Of Discord, Bloodforge.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.69
      win: 0.6
      pick: 0.35
      fit: 0.44
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.66
    Shield of the Phoenix:
      total: 0.55
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.73
    Hydra's Lament:
      total: 0.56
      efficiency: 0.69
      win: 0.55
      pick: 0.28
      fit: 0.37
    Runeforged Hammer:
      total: 0.55
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.54
    Amanita Charm:
      total: 0.59
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.86
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - The Reaper
  - The Crusher
  - Heartseeker
  - Titan's Bane
  flex_slots:
  - The Reaper
  - Titan's Bane
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: The Crusher, The Reaper, Avatar''s Parashu, Avenging Blade, Tekko-Kagi,
    Pendulum Blade, Runeforged Hammer, Blink Rune, Riptalon, Lernaean Bow, Damaru,
    Golden Blade, Genji''s Guard, Arondight, Oath-Sworn Spear, Berserker''s Shield,
    Shield Splitter, Eye of the Storm, Oni Hunter''s Garb, Tyrfing, Yogi''s Necklace,
    Breastplate of Valor, Screeching Gargoyle, Bloodforge.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.68
      efficiency: 0.69
      win: 0.6
      pick: 0.35
      fit: 1.0
    Hydra's Lament:
      total: 0.57
      efficiency: 0.69
      win: 0.55
      pick: 0.28
      fit: 0.48
    The Reaper:
      total: 0.57
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.94
    The Crusher:
      total: 0.62
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 1.0
    Heartseeker:
      total: 0.6
      efficiency: 0.53
      win: 0.57
      pick: 0.25
      fit: 1.0
    Titan's Bane:
      total: 0.57
      efficiency: 0.51
      win: 0.53
      pick: 0.16
      fit: 0.94
  starter: *id001
- source: suggested
  archetype: fun-crit
  slot_order:
  - Golden Blade
  - Lernaean Bow
  - Berserker's Shield
  - Death Metal
  - Damaru
  - Demon Blade
  flex_slots:
  - Demon Blade
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Pharaoh's Curse — magical protection
    swap_item: Pharaoh's Curse
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: For fun — deliberately fights this god's kit (Crit / attack-speed party
    build). Scored on gold-value + flavor fit only; not meta-checked.
  slot_scores:
    Golden Blade:
      total: 0.3
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.57
    Lernaean Bow:
      total: 0.33
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.67
    Berserker's Shield:
      total: 0.31
      efficiency: 0.74
      win: 0.5
      pick: 0.0
      fit: 0.34
    Death Metal:
      total: 0.32
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.66
    Damaru:
      total: 0.33
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.66
    Demon Blade:
      total: 0.31
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 1.0
  fun: true
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - Runeforged Hammer
  - The Reaper
  - The Crusher
  - Heartseeker
  flex_slots:
  - Runeforged Hammer
  - Heartseeker
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: The Crusher, The Reaper, Runeforged Hammer, Avatar''s
    Parashu, Lernaean Bow, Pendulum Blade, Tekko-Kagi, Avenging Blade, Damaru, Blink
    Rune, Arondight, Golden Blade, Shield Splitter, Eye of the Storm, Tyrfing, Genji''s
    Guard, Bloodforge, Riptalon, Transcendence, Berserker''s Shield, Wyrmskin Hide,
    Breastplate of Valor, Musashi''s Dual Swords, Oni Hunter''s Garb.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.68
      efficiency: 0.69
      win: 0.6
      pick: 0.35
      fit: 1.0
    Hydra's Lament:
      total: 0.61
      efficiency: 0.69
      win: 0.55
      pick: 0.28
      fit: 0.71
    Runeforged Hammer:
      total: 0.56
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.62
    The Reaper:
      total: 0.57
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.91
    The Crusher:
      total: 0.62
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 1.0
    Heartseeker:
      total: 0.6
      efficiency: 0.53
      win: 0.57
      pick: 0.25
      fit: 1.0
  starter: *id001
---
