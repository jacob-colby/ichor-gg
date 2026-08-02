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
  - Pendulum Blade
  - The Crusher
  - Heartseeker
  - Titan's Bane
  flex_slots:
  - Titan's Bane
  - Pendulum Blade
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
    this god: The Crusher, Pendulum Blade, The Reaper, Runeforged Hammer, Avenging
    Blade, Shield Splitter, Tekko-Kagi, Damaru, Lernaean Bow, Tyrfing, Eye of the
    Storm, Transcendence, Arondight, Golden Blade, Oath-Sworn Spear, Rage, Bloodforge,
    Wyrmskin Hide, Avatar''s Parashu, Musashi''s Dual Swords, Devourer''s Gauntlet,
    Genji''s Guard, Riptalon.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.52
      win: 0.6
      pick: 0.35
      fit: 1.0
    Hydra's Lament:
      total: 0.53
      efficiency: 0.45
      win: 0.55
      pick: 0.28
      fit: 0.71
    Pendulum Blade:
      total: 0.49
      efficiency: 0.34
      win: 0.5
      pick: 0.0
      fit: 1.0
    The Crusher:
      total: 0.53
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 1.0
    Heartseeker:
      total: 0.54
      efficiency: 0.34
      win: 0.57
      pick: 0.25
      fit: 1.0
    Titan's Bane:
      total: 0.51
      efficiency: 0.37
      win: 0.53
      pick: 0.16
      fit: 0.91
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: burst
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - Pendulum Blade
  - The Crusher
  - Heartseeker
  - Titan's Bane
  flex_slots:
  - Pendulum Blade
  - Titan's Bane
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
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
    god: The Crusher, Pendulum Blade, Runeforged Hammer, The Reaper, Genji''s Guard,
    Arondight, Avenging Blade, Chandra''s Grace, Shield Splitter, Breastplate of Valor,
    Damaru, Lernaean Bow, Tyrfing, Shield of the Phoenix, Eye of the Storm, Transcendence,
    Tekko-Kagi, Spectral Armor, Kinetic Cuirass, Golden Blade, Screeching Gargoyle,
    Eye of Providence, Riptalon.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.52
      win: 0.6
      pick: 0.35
      fit: 0.78
    Hydra's Lament:
      total: 0.5
      efficiency: 0.45
      win: 0.55
      pick: 0.28
      fit: 0.54
    Pendulum Blade:
      total: 0.46
      efficiency: 0.34
      win: 0.5
      pick: 0.0
      fit: 0.78
    The Crusher:
      total: 0.48
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.66
    Heartseeker:
      total: 0.49
      efficiency: 0.34
      win: 0.57
      pick: 0.25
      fit: 0.66
    Titan's Bane:
      total: 0.46
      efficiency: 0.37
      win: 0.53
      pick: 0.16
      fit: 0.56
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Eye of Providence
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Hydra's Lament
  - Amanita Charm
  flex_slots:
  - Shield of the Phoenix
  - Eye of Providence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Spectral Armor — physical protection
    swap_item: Spectral Armor
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Kinetic Cuirass, Shield of the Phoenix, Eye of Providence,
    Runeforged Hammer, Shield Splitter, Chandra''s Grace, Phoenix Feather, Eye of
    the Storm, Spectral Armor, The Crusher, The Reaper, Avenging Blade, Erosion, Spirit
    Robe, Wyrmskin Hide, Golden Blade, Berserker''s Shield, Midgardian Mail, Pharaoh''s
    Curse, Bloodforge, Genji''s Guard, Leviathan''s Hide, Yogi''s Necklace.'
  slot_scores:
    Eye of Providence:
      total: 0.47
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.56
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.52
      win: 0.6
      pick: 0.35
      fit: 0.44
    Kinetic Cuirass:
      total: 0.48
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.66
    Shield of the Phoenix:
      total: 0.48
      efficiency: 0.4
      win: 0.5
      pick: 0.0
      fit: 0.73
    Hydra's Lament:
      total: 0.48
      efficiency: 0.45
      win: 0.55
      pick: 0.28
      fit: 0.37
    Amanita Charm:
      total: 0.51
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.86
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - Pendulum Blade
  - The Crusher
  - Heartseeker
  - Titan's Bane
  flex_slots:
  - Pendulum Blade
  - Hydra's Lament
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
    for this god: The Crusher, Pendulum Blade, The Reaper, Avenging Blade, Tekko-Kagi,
    Runeforged Hammer, Oath-Sworn Spear, Riptalon, Shield Splitter, Damaru, Lernaean
    Bow, Tyrfing, Avatar''s Parashu, Eye of the Storm, Transcendence, Screeching Gargoyle,
    Golden Blade, Arondight, Spectral Armor, Rage, Kinetic Cuirass, Genji''s Guard,
    Eye of Providence.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.52
      win: 0.6
      pick: 0.35
      fit: 1.0
    Hydra's Lament:
      total: 0.49
      efficiency: 0.45
      win: 0.55
      pick: 0.28
      fit: 0.48
    Pendulum Blade:
      total: 0.49
      efficiency: 0.34
      win: 0.5
      pick: 0.0
      fit: 1.0
    The Crusher:
      total: 0.53
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 1.0
    Heartseeker:
      total: 0.54
      efficiency: 0.34
      win: 0.57
      pick: 0.25
      fit: 1.0
    Titan's Bane:
      total: 0.52
      efficiency: 0.37
      win: 0.53
      pick: 0.16
      fit: 0.94
  starter: *id001
- source: suggested
  archetype: fun-crit
  slot_order:
  - Golden Blade
  - Lernaean Bow
  - Tyrfing
  - Death Metal
  - Damaru
  - Demon Blade
  flex_slots:
  - Demon Blade
  - Golden Blade
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
    Golden Blade:
      total: 0.22
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.57
    Lernaean Bow:
      total: 0.23
      efficiency: 0.37
      win: 0.5
      pick: 0.0
      fit: 0.67
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
      total: 0.24
      efficiency: 0.41
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
- source: suggested
  archetype: model
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - Pendulum Blade
  - The Crusher
  - Heartseeker
  - Titan's Bane
  flex_slots:
  - Titan's Bane
  - Hydra's Lament
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
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: The Crusher, Pendulum Blade, The Reaper, Runeforged Hammer,
    Avenging Blade, Shield Splitter, Tekko-Kagi, Damaru, Lernaean Bow, Tyrfing, Eye
    of the Storm, Transcendence, Arondight, Golden Blade, Oath-Sworn Spear, Rage,
    Bloodforge, Wyrmskin Hide, Avatar''s Parashu, Musashi''s Dual Swords, Devourer''s
    Gauntlet, Genji''s Guard, Riptalon.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.52
      win: 0.6
      pick: 0.35
      fit: 1.0
    Hydra's Lament:
      total: 0.53
      efficiency: 0.45
      win: 0.55
      pick: 0.28
      fit: 0.71
    Pendulum Blade:
      total: 0.49
      efficiency: 0.34
      win: 0.5
      pick: 0.0
      fit: 1.0
    The Crusher:
      total: 0.53
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 1.0
    Heartseeker:
      total: 0.54
      efficiency: 0.34
      win: 0.57
      pick: 0.25
      fit: 1.0
    Titan's Bane:
      total: 0.51
      efficiency: 0.37
      win: 0.53
      pick: 0.16
      fit: 0.91
  starter: *id001
---
