---
type: smite-build
god: Artio
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Denmother
  aspect_pick_rate: 0.38
  aspect_win_rate: 0.59
  slot_order:
  - name: Devourer's Gauntlet
    pick_rate: 0.22
    win_rate: 0.57
    alternates:
    - name: Triton's Conch
      pick_rate: 0.11
      win_rate: 0.67
    - name: Shifter's Shield
      pick_rate: 0.11
      win_rate: 0.4
  - name: Sanguine Lash
    pick_rate: 0.13
    win_rate: 0.53
    alternates:
    - name: Stampede
      pick_rate: 0.1
      win_rate: 0.5
    - name: Prophetic Cloak
      pick_rate: 0.09
      win_rate: 0.5
  - name: Freya's Tears
    pick_rate: 0.23
    win_rate: 0.52
    alternates:
    - name: Genji's Guard
      pick_rate: 0.09
      win_rate: 0.5
    - name: Breastplate of Valor
      pick_rate: 0.07
      win_rate: 0.5
  - name: Draconic Scale
    pick_rate: 0.07
    win_rate: 0.78
    alternates:
    - name: Freya's Tears
      pick_rate: 0.21
      win_rate: 0.65
    - name: Shell of Rebuke
      pick_rate: 0.06
      win_rate: 0.25
  - name: Shell of Rebuke
    pick_rate: 0.12
    win_rate: 0.5
    alternates:
    - name: Hide of the Nemean Lion
      pick_rate: 0.07
      win_rate: 0.43
    - name: Freya's Tears
      pick_rate: 0.06
      win_rate: 0.83
  - name: Medal of Defense
    pick_rate: 0.06
    win_rate: 1.0
    alternates:
    - name: Draconic Scale
      pick_rate: 0.08
      win_rate: 0.6
    - name: Mana Tome
      pick_rate: 0.05
      win_rate: 0.67
  community_starters:
  - name: Bumba's Cudgel
    pick_rate: 0.18
    win_rate: 0.46
  - name: Bumba's Hammer
    pick_rate: 0.18
    win_rate: 0.54
  - name: Bluestone Pendant
    pick_rate: 0.15
    win_rate: 0.62
  source_url: https://smitebrain.com/gods/artio/
  last_verified: '2026-10-09'
  god_win_rate: 0.5294117647058824
  god_matches_won: 72
  god_matches_played: 136
  god_division: obsidian
  god_window_start: '2026-10-06'
  god_window_end: '2026-10-09'
  god_matches_analyzed: 2961
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Draconic Scale
  - Amanita Charm
  - Triton's Conch
  flex_slots:
  - Triton's Conch
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Draconic Scale, Rod of Tahuti, Amanita Charm, Jotunn''s Revenge, Kinetic
    Cuirass, Shield Splitter, Genji''s Guard, Breastplate of Valor, Runeforged Hammer,
    Eye of the Storm, Berserker''s Shield, Erosion, Eye of Providence, Shield of the
    Phoenix, Hydra''s Lament, Stone of Binding, Gluttonous Grimoire, Avenging Blade,
    Helm of Radiance, Magi''s Cloak, Midgardian Mail, Mantle Of Discord, Screeching
    Gargoyle, Stampede, Heartseeker, Leviathan''s Hide, Spear of Desolation, Void
    Shield, Daybreak Gavel, Ancile, Rod of Asclepius, Shifter''s Shield, Oni Hunter''s
    Garb, Prophetic Cloak, Soul Gem, Void Stone, Spectral Armor, Spear of the Magus,
    Arondight, Xibalban Effigy.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.51
      pick: 0.0
      fit: 0.39
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.51
      pick: 0.0
      fit: 0.66
    Freya's Tears:
      total: 0.54
      efficiency: 0.61
      win: 0.52
      pick: 0.36
      fit: 0.5
    Draconic Scale:
      total: 0.62
      efficiency: 0.5
      win: 0.78
      pick: 0.12
      fit: 0.56
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.51
      pick: 0.0
      fit: 0.56
    Triton's Conch:
      total: 0.53
      efficiency: 0.44
      win: 0.67
      pick: 0.11
      fit: 0.45
  community_ordered:
  - Freya's Tears
  - Draconic Scale
  - Triton's Conch
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Shield of the Phoenix
  - Freya's Tears
  - Draconic Scale
  - Amanita Charm
  - Triton's Conch
  flex_slots:
  - Freya's Tears
  - Shield of the Phoenix
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Draconic Scale, Amanita Charm, Rod of Tahuti, Jotunn''s Revenge, Shield
    of the Phoenix, Kinetic Cuirass, Rod of Asclepius, Runeforged Hammer, Shield Splitter,
    Genji''s Guard, Soul Gem, Breastplate of Valor, Eye of the Storm, Berserker''s
    Shield, Erosion, Ethereal Staff, Eye of Providence, The Reaper, Yogi''s Necklace,
    Phoenix Feather, Hydra''s Lament, Gluttonous Grimoire, Avenging Blade, Chandra''s
    Grace, Glorious Pridwen, Lifebinder, Stone of Binding, Midgardian Mail, Helm of
    Radiance, Daybreak Gavel, Stampede, Magi''s Cloak, Leviathan''s Hide, Sphere of
    Negation, Void Shield, Ancile, Screeching Gargoyle, Oni Hunter''s Garb, Heartseeker,
    Shifter''s Shield.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.51
      pick: 0.0
      fit: 0.39
    Shield of the Phoenix:
      total: 0.53
      efficiency: 0.53
      win: 0.51
      pick: 0.0
      fit: 0.8
    Freya's Tears:
      total: 0.53
      efficiency: 0.61
      win: 0.52
      pick: 0.36
      fit: 0.46
    Draconic Scale:
      total: 0.62
      efficiency: 0.5
      win: 0.78
      pick: 0.12
      fit: 0.56
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.51
      pick: 0.0
      fit: 0.86
    Triton's Conch:
      total: 0.54
      efficiency: 0.44
      win: 0.67
      pick: 0.11
      fit: 0.49
  community_ordered:
  - Freya's Tears
  - Draconic Scale
  - Triton's Conch
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Jotunn's Revenge
  - Freya's Tears
  - Draconic Scale
  - Amanita Charm
  - Triton's Conch
  flex_slots:
  - Triton's Conch
  - Stone of Binding
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Void Shield — physical protection
    swap_item: Void Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Draconic Scale, Rod of Tahuti, Jotunn''s Revenge, Amanita Charm,
    Stone of Binding, Gluttonous Grimoire, Avenging Blade, Kinetic Cuirass, Screeching
    Gargoyle, Spear of Desolation, Genji''s Guard, Heartseeker, Spear of the Magus,
    Void Shield, Breastplate of Valor, Soul Gem, Void Stone, Obsidian Shard, Shield
    Splitter, Runeforged Hammer, Titan''s Bane, The Crusher, Berserker''s Shield,
    Eye of the Storm, The Reaper, Hydra''s Lament, Erosion, Eye of Providence, Shield
    of the Phoenix, Doom Orb, Helm of Radiance, The World Stone, Pendulum Blade, Dreamer''s
    Idol, Avatar''s Parashu, Magi''s Cloak, Daybreak Gavel, Midgardian Mail, Mantle
    Of Discord, Rod of Asclepius, Shifter''s Shield.'
  slot_scores:
    Stone of Binding:
      total: 0.51
      efficiency: 0.51
      win: 0.51
      pick: 0.0
      fit: 0.68
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.51
      pick: 0.0
      fit: 0.56
    Freya's Tears:
      total: 0.52
      efficiency: 0.61
      win: 0.52
      pick: 0.36
      fit: 0.36
    Draconic Scale:
      total: 0.59
      efficiency: 0.5
      win: 0.78
      pick: 0.12
      fit: 0.4
    Amanita Charm:
      total: 0.52
      efficiency: 0.65
      win: 0.51
      pick: 0.0
      fit: 0.4
    Triton's Conch:
      total: 0.51
      efficiency: 0.44
      win: 0.67
      pick: 0.11
      fit: 0.33
  community_ordered:
  - Freya's Tears
  - Draconic Scale
  - Triton's Conch
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Freya's Tears
  - Nimble Ring
  - Draconic Scale
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
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Draconic Scale, Rod of Tahuti, Berserker''s Shield, Jotunn''s Revenge,
    Amanita Charm, Nimble Ring, Kinetic Cuirass, Golden Blade, Genji''s Guard, Gluttonous
    Grimoire, Breastplate of Valor, Tyrfing, Runeforged Hammer, Soul Gem, Shield Splitter,
    Pharaoh''s Curse, Riptalon, Lernaean Bow, Silverbranch Bow, Shogun''s Ofuda, Toxic
    Blade, Hydra''s Lament, Erosion, Helm of Radiance, Eye of the Storm, Shield of
    the Phoenix, Eye of Providence, Stone of Binding, Daybreak Gavel, Magi''s Cloak,
    The Reaper, Bragi''s Harp, Tekko-Kagi, Screeching Gargoyle, Spear of Desolation,
    Spear of the Magus, Rod of Asclepius, Avenging Blade, Midgardian Mail, Mantle
    Of Discord, Shifter''s Shield.'
  slot_scores:
    Golden Blade:
      total: 0.49
      efficiency: 0.52
      win: 0.51
      pick: 0.0
      fit: 0.55
    Berserker's Shield:
      total: 0.53
      efficiency: 0.68
      win: 0.51
      pick: 0.0
      fit: 0.43
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.72
      win: 0.51
      pick: 0.0
      fit: 0.21
    Freya's Tears:
      total: 0.51
      efficiency: 0.61
      win: 0.52
      pick: 0.36
      fit: 0.31
    Nimble Ring:
      total: 0.5
      efficiency: 0.65
      win: 0.51
      pick: 0.0
      fit: 0.3
    Draconic Scale:
      total: 0.58
      efficiency: 0.5
      win: 0.78
      pick: 0.12
      fit: 0.35
  community_ordered:
  - Freya's Tears
  - Draconic Scale
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Freya's Tears
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Breastplate of Valor
  - Amanita Charm
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Draconic Scale, Jotunn''s Revenge,
    Rod of Tahuti, Genji''s Guard, Breastplate of Valor, Amanita Charm, Shield of
    the Phoenix, Kinetic Cuirass, Spear of Desolation, Hydra''s Lament, Soul Gem,
    Screeching Gargoyle, Chronos'' Pendant, Berserker''s Shield, Shield Splitter,
    Prophetic Cloak, Runeforged Hammer, Gluttonous Grimoire, Helm of Radiance, Gladiator''s
    Shield, Erosion, Eye of Providence, Arondight, Gem of Focus, Eye of the Storm,
    Stone of Binding, Eye of Erebus, Rod of Asclepius, Spear of the Magus, Magi''s
    Cloak, Chandra''s Grace, Midgardian Mail, Glorious Pridwen, Daybreak Gavel, Obsidian
    Shard, Mantle Of Discord, Jade Scepter, Wish-Granting Pearl, Avenging Blade, Shifter''s
    Shield.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.66
      win: 0.5
      pick: 0.14
      fit: 0.48
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.65
      win: 0.5
      pick: 0.11
      fit: 0.48
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.51
      pick: 0.0
      fit: 0.47
    Freya's Tears:
      total: 0.56
      efficiency: 0.61
      win: 0.52
      pick: 0.36
      fit: 0.63
    Draconic Scale:
      total: 0.6
      efficiency: 0.5
      win: 0.78
      pick: 0.12
      fit: 0.43
    Amanita Charm:
      total: 0.52
      efficiency: 0.65
      win: 0.51
      pick: 0.0
      fit: 0.43
  community_ordered:
  - Genji's Guard
  - Breastplate of Valor
  - Freya's Tears
  - Draconic Scale
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Freya's Tears
  - Draconic Scale
  - Amanita Charm
  - Triton's Conch
  flex_slots:
  - Triton's Conch
  - Amanita Charm
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Draconic Scale, Rod of Tahuti, Jotunn''s Revenge,
    Berserker''s Shield, Amanita Charm, Kinetic Cuirass, Shield Splitter, Runeforged
    Hammer, Genji''s Guard, Breastplate of Valor, Golden Blade, Eye of the Storm,
    Gluttonous Grimoire, Hydra''s Lament, Heartseeker, Lernaean Bow, Tekko-Kagi, Spear
    of Desolation, Tyrfing, Avenging Blade, Spear of the Magus, Erosion, Titan''s
    Bane, Eye of Providence, Shield of the Phoenix, Soul Gem, The Crusher, Helm of
    Radiance, Obsidian Shard, Stone of Binding, Pharaoh''s Curse, The Reaper, Nimble
    Ring, Silverbranch Bow, Magi''s Cloak, Shogun''s Ofuda, Screeching Gargoyle, Daybreak
    Gavel, Bragi''s Harp, Toxic Blade, Shifter''s Shield.'
  slot_scores:
    Berserker's Shield:
      total: 0.52
      efficiency: 0.68
      win: 0.51
      pick: 0.0
      fit: 0.35
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.51
      pick: 0.0
      fit: 0.47
    Freya's Tears:
      total: 0.52
      efficiency: 0.61
      win: 0.52
      pick: 0.36
      fit: 0.36
    Draconic Scale:
      total: 0.59
      efficiency: 0.5
      win: 0.78
      pick: 0.12
      fit: 0.4
    Amanita Charm:
      total: 0.52
      efficiency: 0.65
      win: 0.51
      pick: 0.0
      fit: 0.4
    Triton's Conch:
      total: 0.52
      efficiency: 0.44
      win: 0.67
      pick: 0.11
      fit: 0.39
  community_ordered:
  - Freya's Tears
  - Draconic Scale
  - Triton's Conch
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Jotunn's Revenge
  - Freya's Tears
  - Draconic Scale
  - Rod of Tahuti
  - Amanita Charm
  - Triton's Conch
  flex_slots:
  - Freya's Tears
  - Amanita Charm
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Draconic Scale, Rod of Tahuti, Jotunn''s
    Revenge, Triton''s Conch, Amanita Charm, Gluttonous Grimoire, Kinetic Cuirass,
    Genji''s Guard, Spear of Desolation, Breastplate of Valor, Spear of the Magus,
    Shield Splitter, Runeforged Hammer, Soul Gem, Helm of Radiance, Obsidian Shard,
    Berserker''s Shield, Eye of the Storm, Hydra''s Lament, Rod of Asclepius, Heartseeker,
    Erosion, Eye of Providence, Shield of the Phoenix, Doom Orb, Jade Scepter, Death
    Metal, Stone of Binding, Wish-Granting Pearl, Avenging Blade, Chronos'' Pendant,
    The World Stone, Titan''s Bane, The Crusher, Ancient Signet, Magi''s Cloak, Dreamer''s
    Idol, Helm of Darkness, Screeching Gargoyle, Daybreak Gavel, Shifter''s Shield.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.51
      pick: 0.0
      fit: 0.42
    Freya's Tears:
      total: 0.52
      efficiency: 0.61
      win: 0.52
      pick: 0.36
      fit: 0.36
    Draconic Scale:
      total: 0.59
      efficiency: 0.5
      win: 0.78
      pick: 0.12
      fit: 0.4
    Rod of Tahuti:
      total: 0.58
      efficiency: 0.86
      win: 0.51
      pick: 0.0
      fit: 0.34
    Amanita Charm:
      total: 0.52
      efficiency: 0.65
      win: 0.51
      pick: 0.0
      fit: 0.4
    Triton's Conch:
      total: 0.53
      efficiency: 0.44
      win: 0.67
      pick: 0.11
      fit: 0.49
  community_ordered:
  - Freya's Tears
  - Draconic Scale
  - Triton's Conch
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
    Cuirass, Shield Splitter, Shifter''s Shield, Genji''s Guard, Breastplate of Valor,
    Runeforged Hammer, Eye of the Storm, Berserker''s Shield, Erosion, Eye of Providence,
    Draconic Scale, Shield of the Phoenix, Hydra''s Lament, Stone of Binding, Gluttonous
    Grimoire, Avenging Blade, Helm of Radiance, Magi''s Cloak, Midgardian Mail, Mantle
    Of Discord, Screeching Gargoyle, Heartseeker, Leviathan''s Hide, Spear of Desolation,
    Void Shield, Stampede, Daybreak Gavel, Ancile, Rod of Asclepius, Oni Hunter''s
    Garb, Prophetic Cloak, Soul Gem, Void Stone, Spectral Armor, Spear of the Magus,
    Arondight, Xibalban Effigy.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.51
      pick: 0.0
      fit: 0.39
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.51
      pick: 0.0
      fit: 0.66
    Shield Splitter:
      total: 0.51
      efficiency: 0.55
      win: 0.51
      pick: 0.0
      fit: 0.61
    Freya's Tears:
      total: 0.54
      efficiency: 0.61
      win: 0.52
      pick: 0.36
      fit: 0.5
    Shifter's Shield:
      total: 0.46
      efficiency: 0.55
      win: 0.4
      pick: 0.11
      fit: 0.56
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.51
      pick: 0.0
      fit: 0.56
  community_ordered:
  - Freya's Tears
  - Shifter's Shield
  starter: *id001
---
