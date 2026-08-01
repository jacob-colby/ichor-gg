---
type: smite-build
god: Bastet
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Watchful Pride
  aspect_pick_rate: 0.06
  aspect_win_rate: 0.5
  slot_order:
  - name: Jotunn's Revenge
    pick_rate: 0.67
    win_rate: 0.51
    alternates:
    - name: Transcendence
      pick_rate: 0.14
      win_rate: 0.51
    - name: Barbed Carver
      pick_rate: 0.03
      win_rate: 0.67
  - name: Transcendence
    pick_rate: 0.26
    win_rate: 0.54
    alternates:
    - name: Barbed Carver
      pick_rate: 0.2
      win_rate: 0.52
    - name: Jotunn's Revenge
      pick_rate: 0.16
      win_rate: 0.47
  - name: Barbed Carver
    pick_rate: 0.2
    win_rate: 0.52
    alternates:
    - name: The Reaper
      pick_rate: 0.14
      win_rate: 0.53
    - name: Pendulum Blade
      pick_rate: 0.13
      win_rate: 0.51
  - name: Heartseeker
    pick_rate: 0.29
    win_rate: 0.56
    alternates:
    - name: Titan's Bane
      pick_rate: 0.16
      win_rate: 0.6
    - name: The Crusher
      pick_rate: 0.09
      win_rate: 0.35
  - name: Titan's Bane
    pick_rate: 0.18
    win_rate: 0.76
    alternates:
    - name: Heartseeker
      pick_rate: 0.2
      win_rate: 0.51
    - name: Lucerne Hammer
      pick_rate: 0.1
      win_rate: 0.42
  - name: Lucerne Hammer
    pick_rate: 0.1
    win_rate: 0.47
    alternates:
    - name: Titan's Bane
      pick_rate: 0.1
      win_rate: 0.6
    - name: Avatar's Parashu
      pick_rate: 0.07
      win_rate: 0.73
  source_url: https://smitebrain.com/gods/bastet/
  last_verified: '2026-08-01'
  god_win_rate: 0.5176056338028169
  god_matches_won: 147
  god_matches_played: 284
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
  - The Reaper
  - Tekko-Kagi
  - The Crusher
  - Heartseeker
  - Titan's Bane
  flex_slots:
  - Heartseeker
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: The Crusher, The Reaper, Tekko-Kagi, Hydra''s Lament, Pendulum Blade,
    Runeforged Hammer, Avenging Blade, Shield Splitter, Tyrfing, Lernaean Bow, Eye
    of the Storm, Golden Blade, Arondight, Damaru, Oath-Sworn Spear, Rage, Bloodforge,
    Wyrmskin Hide, Musashi''s Dual Swords, Devourer''s Gauntlet, Spectral Armor, Avatar''s
    Parashu, Kinetic Cuirass.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.55
      win: 0.51
      pick: 0.67
      fit: 1.0
    The Reaper:
      total: 0.52
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.91
    Tekko-Kagi:
      total: 0.49
      efficiency: 0.36
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
      total: 0.52
      efficiency: 0.28
      win: 0.56
      pick: 0.29
      fit: 1.0
    Titan's Bane:
      total: 0.59
      efficiency: 0.28
      win: 0.76
      pick: 0.18
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
  - The Reaper
  - Hydra's Lament
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
    god: The Crusher, The Reaper, Hydra''s Lament, Pendulum Blade, Tekko-Kagi, Runeforged
    Hammer, Avenging Blade, Genji''s Guard, Arondight, Shield Splitter, Chandra''s
    Grace, Tyrfing, Lernaean Bow, Breastplate of Valor, Eye of the Storm, Shield of
    the Phoenix, Spectral Armor, Kinetic Cuirass, Golden Blade, Eye of Providence,
    Screeching Gargoyle, Damaru, Oath-Sworn Spear.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.55
      win: 0.51
      pick: 0.67
      fit: 0.78
    Hydra's Lament:
      total: 0.46
      efficiency: 0.44
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
      total: 0.5
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.66
    Heartseeker:
      total: 0.46
      efficiency: 0.28
      win: 0.56
      pick: 0.29
      fit: 0.66
    Titan's Bane:
      total: 0.53
      efficiency: 0.28
      win: 0.76
      pick: 0.18
      fit: 0.56
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Shield Splitter
  - The Reaper
  - The Crusher
  - Titan's Bane
  - Amanita Charm
  flex_slots:
  - The Crusher
  - Shield Splitter
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Eye of Providence — physical protection
    swap_item: Eye of Providence
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: The Reaper, Amanita Charm, The Crusher, Shield Splitter, Kinetic Cuirass,
    Eye of Providence, Shield of the Phoenix, Hydra''s Lament, Runeforged Hammer,
    Spirit Robe, Phoenix Feather, Eye of the Storm, Chandra''s Grace, Spectral Armor,
    Avenging Blade, Bloodforge, Erosion, Genji''s Guard, Tekko-Kagi, Tyrfing, Glorious
    Pridwen, Mantle Of Discord, Shroud of Vengeance, Devourer''s Gauntlet, Lernaean
    Bow, Breastplate of Valor.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.55
      win: 0.51
      pick: 0.67
      fit: 0.44
    Shield Splitter:
      total: 0.46
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.57
    The Reaper:
      total: 0.49
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
    Titan's Bane:
      total: 0.51
      efficiency: 0.28
      win: 0.76
      pick: 0.18
      fit: 0.4
    Amanita Charm:
      total: 0.48
      efficiency: 0.44
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
  - Heartseeker
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
    for this god: The Crusher, The Reaper, Tekko-Kagi, Pendulum Blade, Avenging Blade,
    Hydra''s Lament, Runeforged Hammer, Oath-Sworn Spear, Shield Splitter, Tyrfing,
    Lernaean Bow, Eye of the Storm, Riptalon, Golden Blade, Screeching Gargoyle, Damaru,
    Arondight, Avatar''s Parashu, Spectral Armor, Rage, Kinetic Cuirass, Eye of Providence,
    Genji''s Guard.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.55
      win: 0.51
      pick: 0.67
      fit: 1.0
    The Reaper:
      total: 0.52
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.94
    Tekko-Kagi:
      total: 0.49
      efficiency: 0.36
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
      total: 0.52
      efficiency: 0.28
      win: 0.56
      pick: 0.29
      fit: 1.0
    Titan's Bane:
      total: 0.59
      efficiency: 0.28
      win: 0.76
      pick: 0.18
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
  - Jotunn's Revenge
  - Demon Blade
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
      win: 0.51
      pick: 0.67
      fit: 0.23
    Tyrfing:
      total: 0.23
      efficiency: 0.37
      win: 0.5
      pick: 0.0
      fit: 0.67
    Death Metal:
      total: 0.25
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.66
    Damaru:
      total: 0.23
      efficiency: 0.37
      win: 0.5
      pick: 0.0
      fit: 0.66
    Demon Blade:
      total: 0.22
      efficiency: 0.21
      win: 0.5
      pick: 0.0
      fit: 1.0
  fun: true
  starter: *id001
---
