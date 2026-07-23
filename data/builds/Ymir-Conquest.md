---
type: smite-build
god: Ymir
mode: Conquest
builds:
- source: community
  aspect: null
  aspect_pick_rate: null
  aspect_win_rate: null
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.24
    win_rate: 0.55
    alternates:
    - name: Gauntlet of Thebes
      pick_rate: 0.12
      win_rate: 0.52
    - name: Stampede
      pick_rate: 0.09
      win_rate: 0.48
  - name: Genji's Guard
    pick_rate: 0.15
    win_rate: 0.5
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.12
      win_rate: 0.57
    - name: Stampede
      pick_rate: 0.11
      win_rate: 0.52
  - name: Spirit Robe
    pick_rate: 0.09
    win_rate: 0.48
    alternates:
    - name: Genji's Guard
      pick_rate: 0.12
      win_rate: 0.55
    - name: Dwarven Plate
      pick_rate: 0.08
      win_rate: 0.43
  - name: Dwarven Plate
    pick_rate: 0.08
    win_rate: 0.65
    alternates:
    - name: Spirit Robe
      pick_rate: 0.1
      win_rate: 0.57
    - name: Shell of Rebuke
      pick_rate: 0.07
      win_rate: 0.45
  - name: Engraved Guard
    pick_rate: 0.06
    win_rate: 0.36
    alternates:
    - name: Dwarven Plate
      pick_rate: 0.09
      win_rate: 0.61
    - name: Spirit Robe
      pick_rate: 0.06
      win_rate: 0.71
  - name: Circle of Protection
    pick_rate: 0.07
    win_rate: 0.43
    alternates:
    - name: Engraved Guard
      pick_rate: 0.08
      win_rate: 0.56
    - name: Spirit Robe
      pick_rate: 0.05
      win_rate: 0.6
  source_url: https://smitebrain.com/gods/ymir/
  last_verified: '2026-07-22'
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Eye of Providence
  - Kinetic Cuirass
  - Shifter's Shield
  - Spectral Armor
  - Amanita Charm
  - Erosion
  flex_slots:
  - Erosion
  - Spectral Armor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Kinetic Cuirass, Eye of Providence, Amanita Charm, Erosion, Spectral
    Armor, Genji''s Guard, Shield of the Phoenix, Gladiator''s Shield, Rod of Asclepius,
    Draconic Scale, Gluttonous Grimoire, Ethereal Staff, Prophetic Cloak, Shroud of
    Vengeance, Midgardian Mail, Mantle Of Discord, Magi''s Cloak, Freya''s Tears,
    Phoenix Feather, Leviathan''s Hide, Ancile, Breastplate of Valor, Helm of Radiance,
    Chandra''s Grace, Stone of Binding, Oni Hunter''s Garb.'
  slot_scores:
    Eye of Providence:
      total: 0.45
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.72
    Kinetic Cuirass:
      total: 0.45
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.82
    Shifter's Shield:
      total: 0.44
      efficiency: 0.3
      win: 0.55
      pick: 0.24
      fit: 0.72
    Spectral Armor:
      total: 0.41
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.46
    Amanita Charm:
      total: 0.44
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.72
    Erosion:
      total: 0.42
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.72
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Eye of Providence
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Shifter's Shield
  - Spectral Armor
  - Amanita Charm
  flex_slots:
  - Shifter's Shield
  - Spectral Armor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Phoenix Feather — magical protection
    swap_item: Phoenix Feather
  - vs_tag: physical_heavy
    swap: Spirit Robe — physical protection
    swap_item: Spirit Robe
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Rod of Asclepius, Kinetic Cuirass,
    Eye of Providence, Chandra''s Grace, Phoenix Feather, Soul Gem, Lifebinder, Spectral
    Armor, Blood-Bound Book, Genji''s Guard, Spirit Robe, Erosion, Bancroft''s Talon,
    Gluttonous Grimoire, Ethereal Staff, Glorious Pridwen, Gladiator''s Shield, Midgardian
    Mail, Breastplate of Valor, Leviathan''s Hide, Ancile, Helm of Radiance, Shroud
    of Vengeance, Draconic Scale.'
  slot_scores:
    Eye of Providence:
      total: 0.42
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.53
    Kinetic Cuirass:
      total: 0.42
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.63
    Shield of the Phoenix:
      total: 0.43
      efficiency: 0.4
      win: 0.5
      pick: 0.0
      fit: 0.77
    Shifter's Shield:
      total: 0.41
      efficiency: 0.3
      win: 0.55
      pick: 0.24
      fit: 0.53
    Spectral Armor:
      total: 0.4
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.36
    Amanita Charm:
      total: 0.45
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.83
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Eye of Providence
  - Kinetic Cuirass
  - Gluttonous Grimoire
  - Shifter's Shield
  - Spear of Desolation
  - The Cosmic Horror
  flex_slots:
  - The Cosmic Horror
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Spectral Armor — physical protection
    swap_item: Spectral Armor
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Gluttonous Grimoire, Kinetic Cuirass, Eye of Providence, Soul Gem,
    Amanita Charm, The Cosmic Horror, Spear of Desolation, Screeching Gargoyle, Genji''s
    Guard, Spectral Armor, Void Stone, Stone of Binding, Spear of the Magus, Void
    Shield, Erosion, Doom Orb, Shield of the Phoenix, Rod of Asclepius, Ethereal Staff,
    Obsidian Shard, The World Stone, Midgardian Mail, Gladiator''s Shield, Shroud
    of Vengeance, Chandra''s Grace, Helm of Radiance, Breastplate of Valor.'
  slot_scores:
    Eye of Providence:
      total: 0.41
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.48
    Kinetic Cuirass:
      total: 0.41
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.58
    Gluttonous Grimoire:
      total: 0.42
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.63
    Shifter's Shield:
      total: 0.4
      efficiency: 0.3
      win: 0.55
      pick: 0.24
      fit: 0.48
    Spear of Desolation:
      total: 0.4
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.48
    The Cosmic Horror:
      total: 0.4
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.4
  starter: *id001
- source: suggested
  archetype: fun-crit
  slot_order:
  - Tyrfing
  - Rage
  - Bragi's Harp
  - Death Metal
  - Damaru
  - Demon Blade
  flex_slots:
  - Rage
  - Bragi's Harp
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
    Tyrfing:
      total: 0.24
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.67
    Rage:
      total: 0.23
      efficiency: 0.37
      win: 0.5
      pick: 0.0
      fit: 0.66
    Bragi's Harp:
      total: 0.23
      efficiency: 0.36
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
      efficiency: 0.37
      win: 0.5
      pick: 0.0
      fit: 0.66
    Demon Blade:
      total: 0.23
      efficiency: 0.23
      win: 0.5
      pick: 0.0
      fit: 1.0
  fun: true
  starter: *id001
---
