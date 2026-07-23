---
type: smite-build
god: Bastet
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Watchful Pride
  aspect_pick_rate: 0.07
  aspect_win_rate: 0.48
  slot_order:
  - name: Jotunn's Revenge
    pick_rate: 0.66
    win_rate: 0.56
    alternates:
    - name: Transcendence
      pick_rate: 0.12
      win_rate: 0.65
    - name: Shifter's Shield
      pick_rate: 0.05
      win_rate: 0.38
  - name: Transcendence
    pick_rate: 0.31
    win_rate: 0.59
    alternates:
    - name: Barbed Carver
      pick_rate: 0.17
      win_rate: 0.56
    - name: Jotunn's Revenge
      pick_rate: 0.13
      win_rate: 0.56
  - name: Barbed Carver
    pick_rate: 0.18
    win_rate: 0.57
    alternates:
    - name: Pendulum Blade
      pick_rate: 0.16
      win_rate: 0.56
    - name: The Crusher
      pick_rate: 0.12
      win_rate: 0.6
  - name: Heartseeker
    pick_rate: 0.31
    win_rate: 0.65
    alternates:
    - name: Titan's Bane
      pick_rate: 0.23
      win_rate: 0.52
    - name: The Crusher
      pick_rate: 0.06
      win_rate: 0.67
  - name: Titan's Bane
    pick_rate: 0.27
    win_rate: 0.69
    alternates:
    - name: Heartseeker
      pick_rate: 0.19
      win_rate: 0.54
    - name: Lucerne Hammer
      pick_rate: 0.08
      win_rate: 0.48
  - name: Lucerne Hammer
    pick_rate: 0.09
    win_rate: 0.58
    alternates:
    - name: Heartseeker
      pick_rate: 0.09
      win_rate: 0.6
    - name: Blinking Abyss
      pick_rate: 0.07
      win_rate: 0.74
  source_url: https://smitebrain.com/gods/bastet/
  last_verified: '2026-07-23'
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - The Reaper
  - The Crusher
  - Heartseeker
  - Titan's Bane
  flex_slots:
  - The Reaper
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Spectral Armor — physical protection
    swap_item: Spectral Armor
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: The Crusher, The Reaper, Hydra''s Lament, Tekko-Kagi, Pendulum Blade,
    Runeforged Hammer, Avenging Blade, Shield Splitter, Tyrfing, Eye of the Storm,
    Lernaean Bow, Arondight, Golden Blade, Damaru, Oath-Sworn Spear, Rage, Bloodforge,
    Wyrmskin Hide, Musashi''s Dual Swords, Devourer''s Gauntlet, Genji''s Guard, Spectral
    Armor, Avatar''s Parashu.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.63
      efficiency: 0.55
      win: 0.56
      pick: 0.66
      fit: 1.0
    Transcendence:
      total: 0.5
      efficiency: 0.4
      win: 0.59
      pick: 0.31
      fit: 0.52
    The Reaper:
      total: 0.51
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.91
    The Crusher:
      total: 0.55
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 1.0
    Heartseeker:
      total: 0.56
      efficiency: 0.28
      win: 0.65
      pick: 0.31
      fit: 1.0
    Titan's Bane:
      total: 0.59
      efficiency: 0.37
      win: 0.69
      pick: 0.27
      fit: 0.91
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: burst
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - The Reaper
  - The Crusher
  - Heartseeker
  - Titan's Bane
  flex_slots:
  - Hydra's Lament
  - The Reaper
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: The Crusher, Hydra''s Lament, The Reaper, Pendulum Blade, Runeforged Hammer,
    Tekko-Kagi, Genji''s Guard, Avenging Blade, Arondight, Shield Splitter, Chandra''s
    Grace, Tyrfing, Breastplate of Valor, Eye of the Storm, Lernaean Bow, Shield of
    the Phoenix, Spectral Armor, Golden Blade, Kinetic Cuirass, Screeching Gargoyle,
    Damaru, Eye of Providence, Oath-Sworn Spear.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.55
      win: 0.56
      pick: 0.66
      fit: 0.78
    Hydra's Lament:
      total: 0.46
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.54
    The Reaper:
      total: 0.46
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.56
    The Crusher:
      total: 0.49
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.66
    Heartseeker:
      total: 0.51
      efficiency: 0.28
      win: 0.65
      pick: 0.31
      fit: 0.66
    Titan's Bane:
      total: 0.54
      efficiency: 0.37
      win: 0.69
      pick: 0.27
      fit: 0.56
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - The Reaper
  - The Crusher
  - Heartseeker
  - Titan's Bane
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - The Crusher
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: The Reaper, Amanita Charm, The Crusher, Shield Splitter, Kinetic Cuirass,
    Shield of the Phoenix, Eye of Providence, Hydra''s Lament, Spirit Robe, Runeforged
    Hammer, Phoenix Feather, Eye of the Storm, Chandra''s Grace, Spectral Armor, Bloodforge,
    Genji''s Guard, Avenging Blade, Erosion, Tyrfing, Glorious Pridwen, Devourer''s
    Gauntlet, Tekko-Kagi, Shroud of Vengeance, Mantle Of Discord, Breastplate of Valor,
    Lernaean Bow.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.55
      win: 0.56
      pick: 0.66
      fit: 0.44
    The Reaper:
      total: 0.48
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.7
    The Crusher:
      total: 0.47
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.5
    Heartseeker:
      total: 0.48
      efficiency: 0.28
      win: 0.65
      pick: 0.31
      fit: 0.5
    Titan's Bane:
      total: 0.51
      efficiency: 0.37
      win: 0.69
      pick: 0.27
      fit: 0.4
    Amanita Charm:
      total: 0.48
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.65
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - The Reaper
  - Tekko-Kagi
  - The Crusher
  - Heartseeker
  - Titan's Bane
  flex_slots:
  - The Reaper
  - Tekko-Kagi
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Spectral Armor — physical protection
    swap_item: Spectral Armor
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: The Crusher, The Reaper, Tekko-Kagi, Avenging Blade, Pendulum Blade,
    Hydra''s Lament, Oath-Sworn Spear, Runeforged Hammer, Shield Splitter, Tyrfing,
    Eye of the Storm, Lernaean Bow, Screeching Gargoyle, Riptalon, Golden Blade, Damaru,
    Arondight, Avatar''s Parashu, Rage, Spectral Armor, Genji''s Guard, Kinetic Cuirass,
    Void Stone.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.63
      efficiency: 0.55
      win: 0.56
      pick: 0.66
      fit: 1.0
    The Reaper:
      total: 0.52
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.94
    Tekko-Kagi:
      total: 0.49
      efficiency: 0.35
      win: 0.5
      pick: 0.0
      fit: 0.94
    The Crusher:
      total: 0.55
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 1.0
    Heartseeker:
      total: 0.56
      efficiency: 0.28
      win: 0.65
      pick: 0.31
      fit: 1.0
    Titan's Bane:
      total: 0.59
      efficiency: 0.37
      win: 0.69
      pick: 0.27
      fit: 0.94
  starter: *id001
- source: suggested
  archetype: fun-crit
  slot_order:
  - Lernaean Bow
  - Jotunn's Revenge
  - Tyrfing
  - Death Metal
  - Damaru
  - Demon Blade
  flex_slots:
  - Demon Blade
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: For fun — deliberately fights this god's kit (Crit / attack-speed party
    build). Scored on gold-value + flavor fit only; not meta-checked.
  slot_scores:
    Lernaean Bow:
      total: 0.23
      efficiency: 0.36
      win: 0.5
      pick: 0.0
      fit: 0.67
    Jotunn's Revenge:
      total: 0.23
      efficiency: 0.55
      win: 0.56
      pick: 0.66
      fit: 0.23
    Tyrfing:
      total: 0.24
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.67
    Death Metal:
      total: 0.25
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.66
    Damaru:
      total: 0.23
      efficiency: 0.38
      win: 0.5
      pick: 0.0
      fit: 0.66
    Demon Blade:
      total: 0.23
      efficiency: 0.22
      win: 0.5
      pick: 0.0
      fit: 1.0
  fun: true
  starter: *id001
---
