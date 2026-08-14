---
type: smite-build
god: Athena
mode: Conquest
builds:
- source: community
  aspect: Aspect of War
  aspect_pick_rate: 0.32
  aspect_win_rate: 0.55
  slot_order:
  - name: Stampede
    pick_rate: 0.21
    win_rate: 0.56
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.15
      win_rate: 0.5
    - name: Gauntlet of Thebes
      pick_rate: 0.14
      win_rate: 0.48
  - name: Genji's Guard
    pick_rate: 0.16
    win_rate: 0.52
    alternates:
    - name: Book of Thoth
      pick_rate: 0.1
      win_rate: 0.53
    - name: Breastplate of Valor
      pick_rate: 0.09
      win_rate: 0.5
  - name: Breastplate of Valor
    pick_rate: 0.1
    win_rate: 0.53
    alternates:
    - name: Hydra's Lament
      pick_rate: 0.09
      win_rate: 0.64
    - name: Genji's Guard
      pick_rate: 0.09
      win_rate: 0.38
  - name: Freya's Tears
    pick_rate: 0.08
    win_rate: 0.55
    alternates:
    - name: Genji's Guard
      pick_rate: 0.11
      win_rate: 0.5
    - name: Deathbringer
      pick_rate: 0.08
      win_rate: 0.64
  - name: Deathbringer
    pick_rate: 0.08
    win_rate: 0.6
    alternates:
    - name: Engraved Guard
      pick_rate: 0.07
      win_rate: 0.67
    - name: Dwarven Plate
      pick_rate: 0.06
      win_rate: 0.43
  - name: Engraved Guard
    pick_rate: 0.1
    win_rate: 0.5
    alternates:
    - name: Blinking Abyss
      pick_rate: 0.07
      win_rate: 0.83
    - name: Veve Charm
      pick_rate: 0.07
      win_rate: 0.67
  community_starters:
  - name: Selflessness
    pick_rate: 0.25
    win_rate: 0.51
  - name: Bumba's Hammer
    pick_rate: 0.15
    win_rate: 0.52
  - name: Bumba's Cudgel
    pick_rate: 0.14
    win_rate: 0.45
  source_url: https://smitebrain.com/gods/athena/
  last_verified: '2026-08-14'
  god_win_rate: 0.5032258064516129
  god_matches_won: 78
  god_matches_played: 155
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-14'
  god_matches_analyzed: 3454
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Kinetic Cuirass
  - Hydra's Lament
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Hydra's Lament
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Erosion — magical protection
    swap_item: Erosion
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Kinetic Cuirass, Amanita Charm, Freya''s Tears, Hydra''s Lament, Berserker''s
    Shield, Rod of Tahuti, Gluttonous Grimoire, Erosion, Shield of the Phoenix, Eye
    of Providence, Oni Hunter''s Garb, Shifter''s Shield, Draconic Scale, Spectral
    Armor, Shield Splitter, Jotunn''s Revenge, Pharaoh''s Curse, The Crusher, Leviathan''s
    Hide, Mantle Of Discord, Midgardian Mail, Stone of Binding, Soul Gem, Eye of the
    Storm, Nimble Ring, Magi''s Cloak, Runeforged Hammer, Ancile, Gladiator''s Shield,
    Shogun''s Ofuda, Screeching Gargoyle, Hide of the Nemean Lion, Prophetic Cloak,
    Helm of Radiance, Void Shield, Doublet of Binding, Hussar''s Wings, Chandra''s
    Grace.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.69
      win: 0.52
      pick: 0.22
      fit: 0.37
    Berserker's Shield:
      total: 0.53
      efficiency: 0.66
      win: 0.53
      pick: 0.0
      fit: 0.44
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.59
      win: 0.53
      pick: 0.0
      fit: 0.78
    Hydra's Lament:
      total: 0.53
      efficiency: 0.56
      win: 0.64
      pick: 0.14
      fit: 0.29
    Freya's Tears:
      total: 0.55
      efficiency: 0.59
      win: 0.55
      pick: 0.13
      fit: 0.62
    Amanita Charm:
      total: 0.56
      efficiency: 0.63
      win: 0.53
      pick: 0.0
      fit: 0.68
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Oni Hunter's Garb — magical protection
    swap_item: Oni Hunter's Garb
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Freya''s Tears,
    Soul Gem, Berserker''s Shield, Gluttonous Grimoire, Chandra''s Grace, Rod of Tahuti,
    Rod of Asclepius, Oni Hunter''s Garb, Erosion, Eye of Providence, Shifter''s Shield,
    Phoenix Feather, Draconic Scale, Spectral Armor, Jotunn''s Revenge, Pharaoh''s
    Curse, Leviathan''s Hide, The Crusher, Midgardian Mail, Runeforged Hammer, Eye
    of the Storm, Glorious Pridwen, Lifebinder, Nimble Ring, Shield Splitter, Gladiator''s
    Shield, Ancile, Blood-Bound Book, Shogun''s Ofuda, The Reaper, Hide of the Nemean
    Lion, Void Shield, Doublet of Binding, Mantle Of Discord, Bancroft''s Talon, Stone
    of Binding.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.69
      win: 0.52
      pick: 0.22
      fit: 0.34
    Berserker's Shield:
      total: 0.54
      efficiency: 0.66
      win: 0.53
      pick: 0.0
      fit: 0.46
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.59
      win: 0.53
      pick: 0.0
      fit: 0.76
    Shield of the Phoenix:
      total: 0.57
      efficiency: 0.57
      win: 0.53
      pick: 0.0
      fit: 0.9
    Freya's Tears:
      total: 0.54
      efficiency: 0.59
      win: 0.55
      pick: 0.13
      fit: 0.54
    Amanita Charm:
      total: 0.6
      efficiency: 0.63
      win: 0.53
      pick: 0.0
      fit: 0.96
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Gluttonous Grimoire
  - The Crusher
  - Rod of Tahuti
  flex_slots:
  - Kinetic Cuirass
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Gluttonous Grimoire, The Crusher, Jotunn''s Revenge,
    Kinetic Cuirass, Amanita Charm, Hydra''s Lament, Soul Gem, Freya''s Tears, Stone
    of Binding, Berserker''s Shield, Screeching Gargoyle, Void Shield, The Cosmic
    Horror, Oni Hunter''s Garb, Spear of the Magus, Void Stone, Shield of the Phoenix,
    Spear of Desolation, Avenging Blade, Erosion, Eye of Providence, Spectral Armor,
    Nimble Ring, Shifter''s Shield, Draconic Scale, Obsidian Shard, The Reaper, Pharaoh''s
    Curse, Riptalon, Shield Splitter, Leviathan''s Hide, Midgardian Mail, Runeforged
    Hammer, Silverbranch Bow, Mantle Of Discord, Eye of the Storm, Helm of Radiance,
    Ancile.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.69
      win: 0.52
      pick: 0.22
      fit: 0.26
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.64
      win: 0.53
      pick: 0.0
      fit: 0.47
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.59
      win: 0.53
      pick: 0.0
      fit: 0.58
    Gluttonous Grimoire:
      total: 0.55
      efficiency: 0.63
      win: 0.53
      pick: 0.0
      fit: 0.63
    The Crusher:
      total: 0.53
      efficiency: 0.64
      win: 0.53
      pick: 0.0
      fit: 0.48
    Rod of Tahuti:
      total: 0.57
      efficiency: 0.77
      win: 0.53
      pick: 0.0
      fit: 0.39
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Genji's Guard
  - Berserker's Shield
  - Hydra's Lament
  - Nimble Ring
  - Rod of Tahuti
  flex_slots:
  - Genji's Guard
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Hydra''s Lament, Nimble Ring, Rod of Tahuti, Kinetic
    Cuirass, Amanita Charm, Gluttonous Grimoire, Freya''s Tears, Golden Blade, The
    Crusher, Pharaoh''s Curse, Jotunn''s Revenge, Riptalon, Oni Hunter''s Garb, Soul
    Gem, Shield of the Phoenix, Shogun''s Ofuda, Tyrfing, Runeforged Hammer, Spectral
    Armor, Erosion, Lernaean Bow, Silverbranch Bow, Shield Splitter, Eye of Providence,
    Shifter''s Shield, Draconic Scale, Eye of the Storm, Leviathan''s Hide, Midgardian
    Mail, Mantle Of Discord, Toxic Blade, Stone of Binding, Helm of Radiance, Death
    Metal, Screeching Gargoyle, Yogi''s Necklace, Damaru, Ancile.'
  slot_scores:
    Golden Blade:
      total: 0.5
      efficiency: 0.53
      win: 0.53
      pick: 0.0
      fit: 0.54
    Genji's Guard:
      total: 0.52
      efficiency: 0.69
      win: 0.52
      pick: 0.22
      fit: 0.2
    Berserker's Shield:
      total: 0.53
      efficiency: 0.66
      win: 0.53
      pick: 0.0
      fit: 0.43
    Hydra's Lament:
      total: 0.53
      efficiency: 0.56
      win: 0.64
      pick: 0.14
      fit: 0.27
    Nimble Ring:
      total: 0.52
      efficiency: 0.68
      win: 0.53
      pick: 0.0
      fit: 0.3
    Rod of Tahuti:
      total: 0.52
      efficiency: 0.77
      win: 0.53
      pick: 0.0
      fit: 0.07
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Hydra's Lament
  - Freya's Tears
  flex_slots:
  - Jotunn's Revenge
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    + fit + win/pick). Underrated for this god: Hydra''s Lament, Freya''s Tears, Jotunn''s
    Revenge, Kinetic Cuirass, Shield of the Phoenix, Rod of Tahuti, Amanita Charm,
    Soul Gem, Gluttonous Grimoire, Berserker''s Shield, The Crusher, Screeching Gargoyle,
    Oni Hunter''s Garb, Chronos'' Pendant, Nimble Ring, Chandra''s Grace, Spear of
    Desolation, Gladiator''s Shield, Erosion, Spectral Armor, Eye of Providence, Prophetic
    Cloak, Shifter''s Shield, Shield Splitter, Draconic Scale, Runeforged Hammer,
    Pharaoh''s Curse, Eye of the Storm, Leviathan''s Hide, Gem of Focus, Helm of Radiance,
    Midgardian Mail, Mantle Of Discord, Totem of Death, Stone of Binding, Arondight,
    Death Metal, Rod of Asclepius, The Cosmic Horror.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.69
      win: 0.52
      pick: 0.22
      fit: 0.48
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.64
      win: 0.53
      pick: 0.16
      fit: 0.48
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.64
      win: 0.53
      pick: 0.0
      fit: 0.46
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.59
      win: 0.53
      pick: 0.0
      fit: 0.55
    Hydra's Lament:
      total: 0.57
      efficiency: 0.56
      win: 0.64
      pick: 0.14
      fit: 0.52
    Freya's Tears:
      total: 0.56
      efficiency: 0.59
      win: 0.55
      pick: 0.13
      fit: 0.64
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Hydra's Lament
  - The Crusher
  - Rod of Tahuti
  flex_slots:
  - Kinetic Cuirass
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Hydra''s Lament, Rod of Tahuti, The Crusher,
    Jotunn''s Revenge, Kinetic Cuirass, Berserker''s Shield, Amanita Charm, Gluttonous
    Grimoire, Freya''s Tears, Nimble Ring, Runeforged Hammer, Shield Splitter, Oni
    Hunter''s Garb, Soul Gem, Golden Blade, Eye of the Storm, Shield of the Phoenix,
    Pharaoh''s Curse, Erosion, Spectral Armor, Eye of Providence, The Reaper, Lernaean
    Bow, Shifter''s Shield, Draconic Scale, Death Metal, Avenging Blade, Damaru, The
    Cosmic Horror, Shogun''s Ofuda, Leviathan''s Hide, Spear of the Magus, Midgardian
    Mail, Mantle Of Discord, Stone of Binding, Tekko-Kagi, Spear of Desolation, Helm
    of Radiance, Tyrfing.'
  slot_scores:
    Berserker's Shield:
      total: 0.52
      efficiency: 0.66
      win: 0.53
      pick: 0.0
      fit: 0.36
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.64
      win: 0.53
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.59
      win: 0.53
      pick: 0.0
      fit: 0.52
    Hydra's Lament:
      total: 0.55
      efficiency: 0.56
      win: 0.64
      pick: 0.14
      fit: 0.4
    The Crusher:
      total: 0.53
      efficiency: 0.64
      win: 0.53
      pick: 0.0
      fit: 0.47
    Rod of Tahuti:
      total: 0.54
      efficiency: 0.77
      win: 0.53
      pick: 0.0
      fit: 0.19
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Hydra's Lament
  - Gluttonous Grimoire
  - The Crusher
  - Rod of Tahuti
  flex_slots:
  - Kinetic Cuirass
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Hydra''s Lament, Gluttonous
    Grimoire, The Crusher, Kinetic Cuirass, Jotunn''s Revenge, Amanita Charm, Freya''s
    Tears, Soul Gem, Berserker''s Shield, Nimble Ring, Oni Hunter''s Garb, The Cosmic
    Horror, Runeforged Hammer, Shield Splitter, Shield of the Phoenix, Death Metal,
    Spear of the Magus, Erosion, Spear of Desolation, Eye of the Storm, Helm of Radiance,
    Spectral Armor, Eye of Providence, Shifter''s Shield, Draconic Scale, Rod of Asclepius,
    Pharaoh''s Curse, The Reaper, Obsidian Shard, Leviathan''s Hide, Golden Blade,
    Chronos'' Pendant, Jade Scepter, Midgardian Mail, Avenging Blade, Mantle Of Discord,
    Damaru, Stone of Binding.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.64
      win: 0.53
      pick: 0.0
      fit: 0.41
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.59
      win: 0.53
      pick: 0.0
      fit: 0.52
    Hydra's Lament:
      total: 0.54
      efficiency: 0.56
      win: 0.64
      pick: 0.14
      fit: 0.36
    Gluttonous Grimoire:
      total: 0.54
      efficiency: 0.63
      win: 0.53
      pick: 0.0
      fit: 0.55
    The Crusher:
      total: 0.53
      efficiency: 0.64
      win: 0.53
      pick: 0.0
      fit: 0.43
    Rod of Tahuti:
      total: 0.56
      efficiency: 0.77
      win: 0.53
      pick: 0.0
      fit: 0.33
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Kinetic Cuirass
  - Freya's Tears
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Rod of Tahuti
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Erosion — magical protection
    swap_item: Erosion
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Kinetic Cuirass, Amanita Charm, Freya''s Tears, Berserker''s
    Shield, Rod of Tahuti, Gluttonous Grimoire, Erosion, Shifter''s Shield, Shield
    of the Phoenix, Eye of Providence, Oni Hunter''s Garb, Draconic Scale, Spectral
    Armor, Shield Splitter, Jotunn''s Revenge, Pharaoh''s Curse, The Crusher, Leviathan''s
    Hide, Mantle Of Discord, Midgardian Mail, Stone of Binding, Soul Gem, Eye of the
    Storm, Nimble Ring, Magi''s Cloak, Runeforged Hammer, Ancile, Gladiator''s Shield,
    Shogun''s Ofuda, Screeching Gargoyle, Hide of the Nemean Lion, Prophetic Cloak,
    Helm of Radiance, Void Shield, Doublet of Binding, Hydra''s Lament, Hussar''s
    Wings, Chandra''s Grace.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.69
      win: 0.52
      pick: 0.22
      fit: 0.37
    Berserker's Shield:
      total: 0.53
      efficiency: 0.66
      win: 0.53
      pick: 0.0
      fit: 0.44
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.59
      win: 0.53
      pick: 0.0
      fit: 0.78
    Freya's Tears:
      total: 0.55
      efficiency: 0.59
      win: 0.55
      pick: 0.13
      fit: 0.62
    Rod of Tahuti:
      total: 0.53
      efficiency: 0.77
      win: 0.53
      pick: 0.0
      fit: 0.13
    Amanita Charm:
      total: 0.56
      efficiency: 0.63
      win: 0.53
      pick: 0.0
      fit: 0.68
  starter: *id001
---
