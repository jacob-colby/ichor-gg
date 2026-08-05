---
type: smite-build
god: Sun Wukong
mode: Conquest
builds:
- source: community
  aspect: Aspect of Transformation
  aspect_pick_rate: 0.22
  aspect_win_rate: 0.59
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.35
    win_rate: 0.55
    alternates:
    - name: Mystical Mail
      pick_rate: 0.14
      win_rate: 0.58
    - name: Spear of Desolation
      pick_rate: 0.1
      win_rate: 0.81
  - name: Genji's Guard
    pick_rate: 0.15
    win_rate: 0.52
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.18
      win_rate: 0.47
    - name: Book of Thoth
      pick_rate: 0.08
      win_rate: 0.86
  - name: Soul Gem
    pick_rate: 0.08
    win_rate: 0.77
    alternates:
    - name: Genji's Guard
      pick_rate: 0.21
      win_rate: 0.56
    - name: Breastplate of Valor
      pick_rate: 0.07
      win_rate: 0.58
  - name: Sundering Echo
    pick_rate: 0.2
    win_rate: 0.53
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.12
      win_rate: 0.58
    - name: Genji's Guard
      pick_rate: 0.09
      win_rate: 0.5
  - name: Draconic Scale
    pick_rate: 0.15
    win_rate: 0.59
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.07
      win_rate: 0.6
    - name: Spirit Robe
      pick_rate: 0.06
      win_rate: 0.67
  - name: Freya's Tears
    pick_rate: 0.06
    win_rate: 0.5
    alternates:
    - name: Oracle Staff
      pick_rate: 0.04
      win_rate: 1.0
    - name: Dwarven Plate
      pick_rate: 0.04
      win_rate: 1.0
  source_url: https://smitebrain.com/gods/sun-wukong/
  last_verified: '2026-08-01'
  god_win_rate: 0.5892857142857143
  god_matches_won: 99
  god_matches_played: 168
  god_division: obsidian
  god_window_start: '2026-07-28'
  god_window_end: '2026-08-01'
  god_matches_analyzed: 4952
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Kinetic Cuirass
  - Runeforged Hammer
  - Shifter's Shield
  - Draconic Scale
  flex_slots:
  - Draconic Scale
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Eye of Providence — physical protection
    swap_item: Eye of Providence
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Runeforged Hammer, Berserker''s Shield, Golden Blade, Draconic Scale,
    Kinetic Cuirass, The Crusher, Amanita Charm, Avenging Blade, Hydra''s Lament,
    Lernaean Bow, Jotunn''s Revenge, Genji''s Guard, Eye of Providence, Oni Hunter''s
    Garb, Eye of the Storm, Pharaoh''s Curse, Shield Splitter, Spectral Armor, Yogi''s
    Necklace, Shield of the Phoenix, Damaru, Shogun''s Ofuda, Wyrmskin Hide, Erosion,
    Leviathan''s Hide, Breastplate of Valor, Mantle Of Discord.'
  slot_scores:
    Golden Blade:
      total: 0.54
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.63
    Berserker's Shield:
      total: 0.55
      efficiency: 0.74
      win: 0.5
      pick: 0.0
      fit: 0.48
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.58
    Runeforged Hammer:
      total: 0.56
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.59
    Shifter's Shield:
      total: 0.54
      efficiency: 0.58
      win: 0.55
      pick: 0.35
      fit: 0.48
    Draconic Scale:
      total: 0.54
      efficiency: 0.55
      win: 0.59
      pick: 0.15
      fit: 0.48
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Kinetic Cuirass
  - Runeforged Hammer
  - Shifter's Shield
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Draconic Scale
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
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Berserker''s Shield, Runeforged Hammer, Draconic Scale,
    Kinetic Cuirass, Shield of the Phoenix, Eye of Providence, Genji''s Guard, Oni
    Hunter''s Garb, Golden Blade, The Crusher, Avenging Blade, Pharaoh''s Curse, Eye
    of the Storm, Hydra''s Lament, The Reaper, Chandra''s Grace, Lernaean Bow, Jotunn''s
    Revenge, Shield Splitter, Spectral Armor, Phoenix Feather, Erosion, Riptalon,
    Yogi''s Necklace, Shogun''s Ofuda, Mantle Of Discord.'
  slot_scores:
    Berserker's Shield:
      total: 0.56
      efficiency: 0.74
      win: 0.5
      pick: 0.0
      fit: 0.5
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.67
    Runeforged Hammer:
      total: 0.55
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.55
    Shifter's Shield:
      total: 0.55
      efficiency: 0.58
      win: 0.55
      pick: 0.35
      fit: 0.57
    Draconic Scale:
      total: 0.55
      efficiency: 0.55
      win: 0.59
      pick: 0.15
      fit: 0.57
    Amanita Charm:
      total: 0.59
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.87
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Runeforged Hammer
  - The Crusher
  flex_slots:
  - Berserker's Shield
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Draconic Scale — physical protection
    swap_item: Draconic Scale
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: The Crusher, Jotunn''s Revenge, Avenging Blade, Runeforged Hammer,
    Berserker''s Shield, Genji''s Guard, The Reaper, Hydra''s Lament, Kinetic Cuirass,
    Amanita Charm, Heartseeker, Lernaean Bow, Golden Blade, Oni Hunter''s Garb, Riptalon,
    Avatar''s Parashu, Eye of Providence, Tekko-Kagi, Pharaoh''s Curse, Spectral Armor,
    Void Shield, Eye of the Storm, Yogi''s Necklace, Titan''s Bane, Shield Splitter,
    Damaru, Void Stone, Shield of the Phoenix.'
  slot_scores:
    Avenging Blade:
      total: 0.55
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.74
    Genji's Guard:
      total: 0.52
      efficiency: 0.74
      win: 0.52
      pick: 0.15
      fit: 0.12
    Berserker's Shield:
      total: 0.53
      efficiency: 0.74
      win: 0.5
      pick: 0.0
      fit: 0.32
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.69
      win: 0.5
      pick: 0.0
      fit: 0.59
    Runeforged Hammer:
      total: 0.53
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.44
    The Crusher:
      total: 0.57
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.65
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Lernaean Bow
  - Berserker's Shield
  - Runeforged Hammer
  - Riptalon
  - Pharaoh's Curse
  flex_slots:
  - Pharaoh's Curse
  - Riptalon
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Golden Blade, Runeforged Hammer, Lernaean Bow,
    Pharaoh''s Curse, Riptalon, Genji''s Guard, Kinetic Cuirass, The Crusher, Amanita
    Charm, Hydra''s Lament, Oni Hunter''s Garb, Tyrfing, Avenging Blade, Jotunn''s
    Revenge, Eye of Providence, Shogun''s Ofuda, Eros'' Bow, Spectral Armor, Yogi''s
    Necklace, Eye of the Storm, Breastplate of Valor, Shield of the Phoenix, Damaru,
    Shield Splitter, Mantle Of Discord, The Reaper.'
  slot_scores:
    Golden Blade:
      total: 0.55
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.68
    Lernaean Bow:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.48
    Berserker's Shield:
      total: 0.55
      efficiency: 0.74
      win: 0.5
      pick: 0.0
      fit: 0.47
    Runeforged Hammer:
      total: 0.52
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.37
    Riptalon:
      total: 0.52
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.54
    Pharaoh's Curse:
      total: 0.52
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.47
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Shield of the Phoenix
  - Hydra's Lament
  flex_slots:
  - Shield of the Phoenix
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Genji''s Guard, Hydra''s Lament, Jotunn''s
    Revenge, Berserker''s Shield, Shield of the Phoenix, Breastplate of Valor, Runeforged
    Hammer, Freya''s Tears, Kinetic Cuirass, Amanita Charm, Chandra''s Grace, The
    Crusher, Oni Hunter''s Garb, Eye of Providence, Arondight, Avenging Blade, Pharaoh''s
    Curse, Lernaean Bow, Golden Blade, Spectral Armor, Yogi''s Necklace, Gladiator''s
    Shield, Screeching Gargoyle, Eye of the Storm, Shogun''s Ofuda, Mantle Of Discord,
    Shield Splitter.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.74
      win: 0.52
      pick: 0.15
      fit: 0.44
    Berserker's Shield:
      total: 0.53
      efficiency: 0.74
      win: 0.5
      pick: 0.0
      fit: 0.31
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.67
      win: 0.5
      pick: 0.0
      fit: 0.44
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.69
      win: 0.5
      pick: 0.0
      fit: 0.49
    Shield of the Phoenix:
      total: 0.53
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.57
    Hydra's Lament:
      total: 0.55
      efficiency: 0.69
      win: 0.5
      pick: 0.0
      fit: 0.55
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Kinetic Cuirass
  - Runeforged Hammer
  - The Crusher
  - Amanita Charm
  flex_slots:
  - The Crusher
  - Amanita Charm
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Eye of Providence — magical protection
    swap_item: Eye of Providence
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Runeforged Hammer, Berserker''s Shield, Golden Blade,
    Kinetic Cuirass, The Crusher, Amanita Charm, Avenging Blade, Hydra''s Lament,
    Lernaean Bow, Jotunn''s Revenge, Eye of Providence, Oni Hunter''s Garb, Eye of
    the Storm, Pharaoh''s Curse, Shield Splitter, Genji''s Guard, Spectral Armor,
    Yogi''s Necklace, Shield of the Phoenix, Damaru, Shogun''s Ofuda, Wyrmskin Hide,
    Erosion, Draconic Scale, Leviathan''s Hide, Breastplate of Valor, Mantle Of Discord.'
  slot_scores:
    Golden Blade:
      total: 0.54
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.63
    Berserker's Shield:
      total: 0.55
      efficiency: 0.74
      win: 0.5
      pick: 0.0
      fit: 0.48
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.58
    Runeforged Hammer:
      total: 0.56
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.59
    The Crusher:
      total: 0.54
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.45
    Amanita Charm:
      total: 0.53
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.48
  starter: *id001
---
