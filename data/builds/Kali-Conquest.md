---
type: smite-build
god: Kali
mode: Conquest
builds:
- source: community
  aspect: Aspect of Unbound Destruction
  aspect_pick_rate: 0.15
  aspect_win_rate: 0.54
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.44
    win_rate: 0.48
    alternates:
    - name: Book of Thoth
      pick_rate: 0.18
      win_rate: 0.48
    - name: Tyrfing
      pick_rate: 0.09
      win_rate: 0.47
  - name: Book of Thoth
    pick_rate: 0.18
    win_rate: 0.53
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.16
      win_rate: 0.57
    - name: Doom Orb
      pick_rate: 0.1
      win_rate: 0.49
  - name: Polynomicon
    pick_rate: 0.31
    win_rate: 0.5
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.09
      win_rate: 0.42
    - name: Hastened Fatalis
      pick_rate: 0.06
      win_rate: 0.42
  - name: Rod of Tahuti
    pick_rate: 0.26
    win_rate: 0.52
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.1
      win_rate: 0.5
    - name: Blinking Abyss
      pick_rate: 0.09
      win_rate: 0.31
  - name: Obsidian Shard
    pick_rate: 0.2
    win_rate: 0.56
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.16
      win_rate: 0.6
    - name: Qin's Blade
      pick_rate: 0.07
      win_rate: 0.57
  - name: Blinking Abyss
    pick_rate: 0.13
    win_rate: 0.59
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.1
      win_rate: 0.55
    - name: Evil Eye
      pick_rate: 0.08
      win_rate: 0.28
  source_url: https://smitebrain.com/gods/kali/
  last_verified: '2026-07-23'
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Lernaean Bow
  - Jotunn's Revenge
  - Tyrfing
  - The Reaper
  - Tekko-Kagi
  - The Crusher
  flex_slots:
  - The Reaper
  - Lernaean Bow
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
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Jotunn''s Revenge, The Crusher, Tekko-Kagi, Tyrfing, The Reaper, Lernaean
    Bow, Hydra''s Lament, Golden Blade, Runeforged Hammer, Damaru, Titan''s Bane,
    Avenging Blade, Rage, Shield Splitter, Berserker''s Shield, Demon Blade, Heartseeker,
    Eye of the Storm, Transcendence, Pendulum Blade, Musashi''s Dual Swords, Spectral
    Armor, Pharaoh''s Curse, Arondight, Barbed Carver, Kinetic Cuirass, Eros'' Bow,
    Oath-Sworn Spear.'
  slot_scores:
    Lernaean Bow:
      total: 0.45
      efficiency: 0.36
      win: 0.5
      pick: 0.0
      fit: 0.63
    Jotunn's Revenge:
      total: 0.5
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.52
    Tyrfing:
      total: 0.45
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.63
    The Reaper:
      total: 0.45
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.47
    Tekko-Kagi:
      total: 0.46
      efficiency: 0.35
      win: 0.5
      pick: 0.0
      fit: 0.74
    The Crusher:
      total: 0.48
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.57
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - The Reaper
  - The Crusher
  - Amanita Charm
  flex_slots:
  - Shield Splitter
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Eye of Providence — magical protection
    swap_item: Eye of Providence
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: The Reaper, Amanita Charm, Jotunn''s Revenge, The Crusher, Shield Splitter,
    Shield of the Phoenix, Kinetic Cuirass, Eye of Providence, Hydra''s Lament, Chandra''s
    Grace, Tyrfing, Spirit Robe, Runeforged Hammer, Phoenix Feather, Berserker''s
    Shield, Spectral Armor, Lernaean Bow, Tekko-Kagi, Genji''s Guard, Bloodforge,
    Eye of the Storm, Golden Blade, Avenging Blade, Riptalon, Damaru, Pharaoh''s Curse,
    Erosion, Devourer''s Gauntlet.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.46
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.31
    Kinetic Cuirass:
      total: 0.43
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.35
    Shield Splitter:
      total: 0.44
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.41
    The Reaper:
      total: 0.47
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.58
    The Crusher:
      total: 0.45
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.38
    Amanita Charm:
      total: 0.46
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.55
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Jotunn's Revenge
  - The Reaper
  - Tekko-Kagi
  - The Crusher
  - Titan's Bane
  flex_slots:
  - Avenging Blade
  - Titan's Bane
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, The Crusher, The Reaper, Tekko-Kagi, Avenging
    Blade, Titan''s Bane, Tyrfing, Hydra''s Lament, Oath-Sworn Spear, Heartseeker,
    Runeforged Hammer, Lernaean Bow, Pendulum Blade, Golden Blade, Damaru, Screeching
    Gargoyle, Shield Splitter, Riptalon, Rage, Berserker''s Shield, Spectral Armor,
    Eye of the Storm, Transcendence, Kinetic Cuirass, Genji''s Guard, Void Stone,
    Eye of Providence, Pharaoh''s Curse.'
  slot_scores:
    Avenging Blade:
      total: 0.46
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 0.6
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.64
    The Reaper:
      total: 0.47
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.6
    Tekko-Kagi:
      total: 0.47
      efficiency: 0.35
      win: 0.5
      pick: 0.0
      fit: 0.8
    The Crusher:
      total: 0.5
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.7
    Titan's Bane:
      total: 0.44
      efficiency: 0.37
      win: 0.5
      pick: 0.0
      fit: 0.6
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
      win: 0.5
      pick: 0.0
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
