---
type: smite-build
god: Artio
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Denmother
  aspect_pick_rate: 0.5
  aspect_win_rate: 0.56
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.16
    win_rate: 0.53
    alternates:
    - name: Lifebinder
      pick_rate: 0.16
      win_rate: 0.59
    - name: Daybreak Gavel
      pick_rate: 0.13
      win_rate: 0.64
  - name: Genji's Guard
    pick_rate: 0.13
    win_rate: 0.57
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.13
      win_rate: 0.71
    - name: Breastplate of Valor
      pick_rate: 0.12
      win_rate: 0.54
  - name: Freya's Tears
    pick_rate: 0.17
    win_rate: 0.56
    alternates:
    - name: Genji's Guard
      pick_rate: 0.12
      win_rate: 0.42
    - name: Gladiator's Shield
      pick_rate: 0.07
      win_rate: 0.86
  - name: Shell of Rebuke
    pick_rate: 0.17
    win_rate: 0.47
    alternates:
    - name: Genji's Guard
      pick_rate: 0.09
      win_rate: 0.56
    - name: Ethereal Staff
      pick_rate: 0.07
      win_rate: 1.0
  - name: Engraved Guard
    pick_rate: 0.05
    win_rate: 0.0
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.1
      win_rate: 0.75
    - name: Freya's Tears
      pick_rate: 0.08
      win_rate: 0.43
  - name: Ring of Dispel
    pick_rate: 0.06
    win_rate: 1.0
    alternates:
    - name: Veve Charm
      pick_rate: 0.06
      win_rate: 0.33
    - name: Draconic Scale
      pick_rate: 0.06
      win_rate: 0.33
  community_starters:
  - name: Bluestone Pendant
    pick_rate: 0.25
    win_rate: 0.48
  - name: Selflessness
    pick_rate: 0.19
    win_rate: 0.33
  - name: Bluestone Brooch
    pick_rate: 0.18
    win_rate: 0.63
  source_url: https://smitebrain.com/gods/artio/
  last_verified: '2026-08-28'
  god_win_rate: 0.5185185185185185
  god_matches_won: 56
  god_matches_played: 108
  god_division: obsidian
  god_window_start: '2026-08-25'
  god_window_end: '2026-08-28'
  god_matches_analyzed: 3498
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Gladiator's Shield
  - Ethereal Staff
  - Freya's Tears
  flex_slots:
  - Kinetic Cuirass
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Amanita Charm, Jotunn''s Revenge, Kinetic Cuirass, Shield
    Splitter, Daybreak Gavel, Runeforged Hammer, Eye of the Storm, Berserker''s Shield,
    Erosion, Eye of Providence, Shield of the Phoenix, Hydra''s Lament, Stone of Binding,
    Gluttonous Grimoire, Avenging Blade, Helm of Radiance, Magi''s Cloak, Midgardian
    Mail, Mantle Of Discord, Screeching Gargoyle, Hide of the Nemean Lion, Heartseeker,
    Leviathan''s Hide, Spear of Desolation, Void Shield, Stampede, Ancile, Rod of
    Asclepius, Oni Hunter''s Garb, Prophetic Cloak, Soul Gem, Void Stone, Spectral
    Armor, Spear of the Magus, Arondight, Xibalban Effigy.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.66
      win: 0.57
      pick: 0.18
      fit: 0.31
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.56
      pick: 0.0
      fit: 0.39
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.56
      pick: 0.0
      fit: 0.66
    Gladiator's Shield:
      total: 0.62
      efficiency: 0.39
      win: 0.86
      pick: 0.11
      fit: 0.58
    Ethereal Staff:
      total: 0.67
      efficiency: 0.46
      win: 1.0
      pick: 0.12
      fit: 0.33
    Freya's Tears:
      total: 0.55
      efficiency: 0.61
      win: 0.56
      pick: 0.26
      fit: 0.5
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Gladiator's Shield
  - Ethereal Staff
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Ethereal Staff, Amanita Charm, Rod of Tahuti, Jotunn''s Revenge, Shield
    of the Phoenix, Kinetic Cuirass, Rod of Asclepius, Daybreak Gavel, Runeforged
    Hammer, Shield Splitter, Soul Gem, Eye of the Storm, Berserker''s Shield, Erosion,
    Eye of Providence, The Reaper, Yogi''s Necklace, Phoenix Feather, Hydra''s Lament,
    Gluttonous Grimoire, Avenging Blade, Chandra''s Grace, Glorious Pridwen, Stone
    of Binding, Midgardian Mail, Helm of Radiance, Hide of the Nemean Lion, Magi''s
    Cloak, Leviathan''s Hide, Sphere of Negation, Void Shield, Stampede, Ancile, Screeching
    Gargoyle, Oni Hunter''s Garb, Heartseeker.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.56
      pick: 0.0
      fit: 0.39
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.56
      pick: 0.0
      fit: 0.66
    Gladiator's Shield:
      total: 0.62
      efficiency: 0.39
      win: 0.86
      pick: 0.11
      fit: 0.6
    Ethereal Staff:
      total: 0.72
      efficiency: 0.46
      win: 1.0
      pick: 0.12
      fit: 0.67
    Freya's Tears:
      total: 0.55
      efficiency: 0.61
      win: 0.56
      pick: 0.26
      fit: 0.46
    Amanita Charm:
      total: 0.61
      efficiency: 0.65
      win: 0.56
      pick: 0.0
      fit: 0.86
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Jotunn's Revenge
  - Gladiator's Shield
  - Ethereal Staff
  - Freya's Tears
  - Rod of Tahuti
  flex_slots:
  - Freya's Tears
  - Stone of Binding
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Jotunn''s Revenge, Amanita Charm, Stone of Binding,
    Gluttonous Grimoire, Avenging Blade, Kinetic Cuirass, Screeching Gargoyle, Daybreak
    Gavel, Spear of Desolation, Heartseeker, Spear of the Magus, Void Shield, Soul
    Gem, Void Stone, Obsidian Shard, Shield Splitter, Runeforged Hammer, Titan''s
    Bane, The Crusher, Berserker''s Shield, Eye of the Storm, The Reaper, Hydra''s
    Lament, Erosion, Eye of Providence, Shield of the Phoenix, Doom Orb, Helm of Radiance,
    The World Stone, Pendulum Blade, Dreamer''s Idol, Avatar''s Parashu, Magi''s Cloak,
    Midgardian Mail, Mantle Of Discord, Rod of Asclepius.'
  slot_scores:
    Stone of Binding:
      total: 0.53
      efficiency: 0.51
      win: 0.56
      pick: 0.0
      fit: 0.68
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.56
      pick: 0.0
      fit: 0.56
    Gladiator's Shield:
      total: 0.6
      efficiency: 0.39
      win: 0.86
      pick: 0.11
      fit: 0.45
    Ethereal Staff:
      total: 0.66
      efficiency: 0.46
      win: 1.0
      pick: 0.12
      fit: 0.26
    Freya's Tears:
      total: 0.53
      efficiency: 0.61
      win: 0.56
      pick: 0.26
      fit: 0.36
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.86
      win: 0.56
      pick: 0.0
      fit: 0.35
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Gladiator's Shield
  - Nimble Ring
  - Ethereal Staff
  flex_slots:
  - Nimble Ring
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Berserker''s Shield, Jotunn''s Revenge, Amanita Charm,
    Nimble Ring, Daybreak Gavel, Kinetic Cuirass, Golden Blade, Gluttonous Grimoire,
    Tyrfing, Runeforged Hammer, Soul Gem, Shield Splitter, Pharaoh''s Curse, Riptalon,
    Lernaean Bow, Silverbranch Bow, Shogun''s Ofuda, Toxic Blade, Hydra''s Lament,
    Erosion, Helm of Radiance, Eye of the Storm, Shield of the Phoenix, Eye of Providence,
    Stone of Binding, Magi''s Cloak, The Reaper, Bragi''s Harp, Tekko-Kagi, Screeching
    Gargoyle, Spear of Desolation, Spear of the Magus, Rod of Asclepius, Avenging
    Blade, Midgardian Mail, Mantle Of Discord.'
  slot_scores:
    Golden Blade:
      total: 0.52
      efficiency: 0.52
      win: 0.56
      pick: 0.0
      fit: 0.55
    Berserker's Shield:
      total: 0.55
      efficiency: 0.68
      win: 0.56
      pick: 0.0
      fit: 0.43
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.72
      win: 0.56
      pick: 0.0
      fit: 0.21
    Gladiator's Shield:
      total: 0.59
      efficiency: 0.39
      win: 0.86
      pick: 0.11
      fit: 0.4
    Nimble Ring:
      total: 0.53
      efficiency: 0.65
      win: 0.56
      pick: 0.0
      fit: 0.3
    Ethereal Staff:
      total: 0.65
      efficiency: 0.46
      win: 1.0
      pick: 0.12
      fit: 0.24
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Gladiator's Shield
  - Ethereal Staff
  - Freya's Tears
  flex_slots:
  - Genji's Guard
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Gladiator''s Shield, Jotunn''s Revenge,
    Rod of Tahuti, Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Spear of
    Desolation, Hydra''s Lament, Daybreak Gavel, Soul Gem, Screeching Gargoyle, Chronos''
    Pendant, Berserker''s Shield, Shield Splitter, Prophetic Cloak, Runeforged Hammer,
    Gluttonous Grimoire, Helm of Radiance, Erosion, Eye of Providence, Arondight,
    Gem of Focus, Eye of the Storm, Stone of Binding, Eye of Erebus, Rod of Asclepius,
    Spear of the Magus, Magi''s Cloak, Chandra''s Grace, Midgardian Mail, Glorious
    Pridwen, Obsidian Shard, Mantle Of Discord, Jade Scepter, Hide of the Nemean Lion,
    Wish-Granting Pearl, Avenging Blade.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.66
      win: 0.57
      pick: 0.18
      fit: 0.48
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.65
      win: 0.54
      pick: 0.16
      fit: 0.48
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.56
      pick: 0.0
      fit: 0.47
    Gladiator's Shield:
      total: 0.64
      efficiency: 0.39
      win: 0.86
      pick: 0.11
      fit: 0.71
    Ethereal Staff:
      total: 0.67
      efficiency: 0.46
      win: 1.0
      pick: 0.12
      fit: 0.33
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.56
      pick: 0.26
      fit: 0.63
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Gladiator's Shield
  - Ethereal Staff
  - Freya's Tears
  flex_slots:
  - Freya's Tears
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge, Berserker''s
    Shield, Amanita Charm, Kinetic Cuirass, Daybreak Gavel, Shield Splitter, Runeforged
    Hammer, Golden Blade, Eye of the Storm, Gluttonous Grimoire, Hydra''s Lament,
    Heartseeker, Lernaean Bow, Tekko-Kagi, Spear of Desolation, Tyrfing, Avenging
    Blade, Spear of the Magus, Erosion, Titan''s Bane, Eye of Providence, Shield of
    the Phoenix, Soul Gem, The Crusher, Helm of Radiance, Obsidian Shard, Stone of
    Binding, Pharaoh''s Curse, The Reaper, Nimble Ring, Silverbranch Bow, Magi''s
    Cloak, Shogun''s Ofuda, Screeching Gargoyle, Bragi''s Harp, Toxic Blade.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.66
      win: 0.57
      pick: 0.18
      fit: 0.22
    Berserker's Shield:
      total: 0.54
      efficiency: 0.68
      win: 0.56
      pick: 0.0
      fit: 0.35
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.56
      pick: 0.0
      fit: 0.47
    Gladiator's Shield:
      total: 0.6
      efficiency: 0.39
      win: 0.86
      pick: 0.11
      fit: 0.44
    Ethereal Staff:
      total: 0.66
      efficiency: 0.46
      win: 1.0
      pick: 0.12
      fit: 0.26
    Freya's Tears:
      total: 0.53
      efficiency: 0.61
      win: 0.56
      pick: 0.26
      fit: 0.36
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Gladiator's Shield
  - Ethereal Staff
  - Freya's Tears
  flex_slots:
  - Genji's Guard
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Amanita Charm, Gluttonous Grimoire, Kinetic Cuirass, Daybreak Gavel, Spear of
    Desolation, Spear of the Magus, Shield Splitter, Runeforged Hammer, Soul Gem,
    Helm of Radiance, Obsidian Shard, Berserker''s Shield, Eye of the Storm, Hydra''s
    Lament, Rod of Asclepius, Heartseeker, Erosion, Eye of Providence, Shield of the
    Phoenix, Doom Orb, Jade Scepter, Death Metal, Stone of Binding, Wish-Granting
    Pearl, Avenging Blade, Chronos'' Pendant, The World Stone, Titan''s Bane, The
    Crusher, Ancient Signet, Magi''s Cloak, Triton''s Conch, Dreamer''s Idol, Helm
    of Darkness, Screeching Gargoyle.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.66
      win: 0.57
      pick: 0.18
      fit: 0.22
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.56
      pick: 0.0
      fit: 0.42
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.56
      win: 0.56
      pick: 0.0
      fit: 0.5
    Gladiator's Shield:
      total: 0.6
      efficiency: 0.39
      win: 0.86
      pick: 0.11
      fit: 0.44
    Ethereal Staff:
      total: 0.68
      efficiency: 0.46
      win: 1.0
      pick: 0.12
      fit: 0.41
    Freya's Tears:
      total: 0.53
      efficiency: 0.61
      win: 0.56
      pick: 0.26
      fit: 0.36
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Shield Splitter
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Rod of Tahuti, Amanita Charm, Jotunn''s Revenge, Kinetic
    Cuirass, Shield Splitter, Runeforged Hammer, Eye of the Storm, Berserker''s Shield,
    Erosion, Eye of Providence, Shield of the Phoenix, Hydra''s Lament, Stone of Binding,
    Gluttonous Grimoire, Avenging Blade, Helm of Radiance, Magi''s Cloak, Midgardian
    Mail, Mantle Of Discord, Screeching Gargoyle, Hide of the Nemean Lion, Heartseeker,
    Leviathan''s Hide, Spear of Desolation, Void Shield, Stampede, Daybreak Gavel,
    Ancile, Rod of Asclepius, Oni Hunter''s Garb, Prophetic Cloak, Soul Gem, Void
    Stone, Spectral Armor, Spear of the Magus, Arondight, Xibalban Effigy.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.56
      pick: 0.0
      fit: 0.39
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.56
      pick: 0.0
      fit: 0.66
    Shield Splitter:
      total: 0.54
      efficiency: 0.55
      win: 0.56
      pick: 0.0
      fit: 0.61
    Freya's Tears:
      total: 0.55
      efficiency: 0.61
      win: 0.56
      pick: 0.26
      fit: 0.5
    Shifter's Shield:
      total: 0.52
      efficiency: 0.55
      win: 0.53
      pick: 0.16
      fit: 0.56
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.56
      pick: 0.0
      fit: 0.56
  starter: *id001
---
