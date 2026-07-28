---
type: smite-build
god: Cabrakan
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Rotund Jotunn
  aspect_pick_rate: 0.04
  aspect_win_rate: 0.41
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.44
    win_rate: 0.54
    alternates:
    - name: Runeforged Hammer
      pick_rate: 0.35
      win_rate: 0.52
    - name: Gauntlet of Thebes
      pick_rate: 0.03
      win_rate: 0.62
  - name: Genji's Guard
    pick_rate: 0.19
    win_rate: 0.58
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.18
      win_rate: 0.45
    - name: Breastplate of Valor
      pick_rate: 0.14
      win_rate: 0.47
  - name: Breastplate of Valor
    pick_rate: 0.15
    win_rate: 0.53
    alternates:
    - name: Genji's Guard
      pick_rate: 0.23
      win_rate: 0.47
    - name: Dwarven Plate
      pick_rate: 0.1
      win_rate: 0.49
  - name: Dwarven Plate
    pick_rate: 0.19
    win_rate: 0.54
    alternates:
    - name: Genji's Guard
      pick_rate: 0.15
      win_rate: 0.61
    - name: Breastplate of Valor
      pick_rate: 0.07
      win_rate: 0.61
  - name: Spirit Robe
    pick_rate: 0.06
    win_rate: 0.56
    alternates:
    - name: Dwarven Plate
      pick_rate: 0.13
      win_rate: 0.64
    - name: Shell of Rebuke
      pick_rate: 0.05
      win_rate: 0.45
  - name: Engraved Guard
    pick_rate: 0.11
    win_rate: 0.56
    alternates:
    - name: Dwarven Plate
      pick_rate: 0.09
      win_rate: 0.63
    - name: Shell of Rebuke
      pick_rate: 0.05
      win_rate: 0.59
  source_url: https://smitebrain.com/gods/cabrakan/
  last_verified: '2026-07-25'
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
  god_win_rate: 0.5229083665338645
  god_matches_won: 525
  god_matches_played: 1004
  god_division: obsidian
  god_window_start: '2026-07-14'
  god_window_end: '2026-07-27'
  god_matches_analyzed: 17172
- source: suggested
  archetype: core
  slot_order:
  - Eye of Providence
  - Genji's Guard
  - Kinetic Cuirass
  - Shifter's Shield
  - Amanita Charm
  - Erosion
  flex_slots:
  - Shifter's Shield
  - Erosion
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Spirit Robe — magical protection
    swap_item: Spirit Robe
  - vs_tag: physical_heavy
    swap: Spectral Armor — physical protection
    swap_item: Spectral Armor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Kinetic Cuirass, Eye of Providence, Amanita Charm, Erosion, Spectral
    Armor, Shield of the Phoenix, Breastplate of Valor, Gluttonous Grimoire, Draconic
    Scale, Gladiator''s Shield, Midgardian Mail, Ethereal Staff, Rod of Asclepius,
    Freya''s Tears, Mantle Of Discord, Chandra''s Grace, Prophetic Cloak, Leviathan''s
    Hide, Shroud of Vengeance, Ancile, Phoenix Feather, Oni Hunter''s Garb, Magi''s
    Cloak, Soul Gem, Screeching Gargoyle.'
  slot_scores:
    Eye of Providence:
      total: 0.5
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.73
    Genji's Guard:
      total: 0.49
      efficiency: 0.46
      win: 0.58
      pick: 0.19
      fit: 0.4
    Kinetic Cuirass:
      total: 0.5
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.83
    Shifter's Shield:
      total: 0.48
      efficiency: 0.29
      win: 0.54
      pick: 0.44
      fit: 0.73
    Amanita Charm:
      total: 0.49
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.73
    Erosion:
      total: 0.47
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.73
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Eye of Providence
  - Genji's Guard
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Spectral Armor
  - Amanita Charm
  flex_slots:
  - Eye of Providence
  - Spectral Armor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Spirit Robe — magical protection
    swap_item: Spirit Robe
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Eye of Providence,
    Rod of Asclepius, Chandra''s Grace, Spirit Robe, Soul Gem, Phoenix Feather, Spectral
    Armor, Erosion, Lifebinder, Blood-Bound Book, Breastplate of Valor, Gluttonous
    Grimoire, Bancroft''s Talon, Ethereal Staff, Gladiator''s Shield, Glorious Pridwen,
    Midgardian Mail, Leviathan''s Hide, Ancile, Oni Hunter''s Garb, Draconic Scale,
    Yogi''s Necklace.'
  slot_scores:
    Eye of Providence:
      total: 0.47
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.54
    Genji's Guard:
      total: 0.48
      efficiency: 0.46
      win: 0.58
      pick: 0.19
      fit: 0.3
    Kinetic Cuirass:
      total: 0.48
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.64
    Shield of the Phoenix:
      total: 0.48
      efficiency: 0.4
      win: 0.5
      pick: 0.0
      fit: 0.78
    Spectral Armor:
      total: 0.45
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.36
    Amanita Charm:
      total: 0.51
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.84
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Eye of Providence
  - Genji's Guard
  - Kinetic Cuirass
  - Gluttonous Grimoire
  - The Cosmic Horror
  - Spectral Armor
  flex_slots:
  - The Cosmic Horror
  - Spectral Armor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Gluttonous Grimoire, Kinetic Cuirass, Eye of Providence, Soul Gem,
    Amanita Charm, The Cosmic Horror, Spectral Armor, Spear of Desolation, Screeching
    Gargoyle, Void Stone, Erosion, Stone of Binding, Breastplate of Valor, Void Shield,
    Spear of the Magus, Shield of the Phoenix, Doom Orb, Ethereal Staff, Rod of Asclepius,
    The World Stone, Chandra''s Grace, Obsidian Shard, Midgardian Mail, Gladiator''s
    Shield, Leviathan''s Hide, Ancile.'
  slot_scores:
    Eye of Providence:
      total: 0.47
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.5
    Genji's Guard:
      total: 0.47
      efficiency: 0.46
      win: 0.58
      pick: 0.19
      fit: 0.27
    Kinetic Cuirass:
      total: 0.47
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.6
    Gluttonous Grimoire:
      total: 0.47
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.65
    The Cosmic Horror:
      total: 0.45
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.4
    Spectral Armor:
      total: 0.45
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.32
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
      total: 0.22
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.23
    Tyrfing:
      total: 0.23
      efficiency: 0.37
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
      total: 0.22
      efficiency: 0.21
      win: 0.5
      pick: 0.0
      fit: 1.0
  fun: true
  starter: *id001
---
