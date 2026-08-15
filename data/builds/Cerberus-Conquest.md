---
type: smite-build
god: Cerberus
mode: Conquest
builds:
- source: community
  aspect: Aspect of Souls
  aspect_pick_rate: 0.05
  aspect_win_rate: 0.3
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.27
    win_rate: 0.54
    alternates:
    - name: Gauntlet of Thebes
      pick_rate: 0.25
      win_rate: 0.6
    - name: Stampede
      pick_rate: 0.09
      win_rate: 0.53
  - name: Genji's Guard
    pick_rate: 0.21
    win_rate: 0.49
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.14
      win_rate: 0.57
    - name: Breastplate of Valor
      pick_rate: 0.14
      win_rate: 0.45
  - name: Shell of Rebuke
    pick_rate: 0.14
    win_rate: 0.57
    alternates:
    - name: Genji's Guard
      pick_rate: 0.15
      win_rate: 0.58
    - name: Stampede
      pick_rate: 0.11
      win_rate: 0.65
  - name: Freya's Tears
    pick_rate: 0.08
    win_rate: 0.6
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.13
      win_rate: 0.58
    - name: Genji's Guard
      pick_rate: 0.1
      win_rate: 0.47
  - name: Hide of the Nemean Lion
    pick_rate: 0.08
    win_rate: 0.54
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.07
      win_rate: 0.82
    - name: Freya's Tears
      pick_rate: 0.07
      win_rate: 0.73
  - name: Captain's Ring
    pick_rate: 0.07
    win_rate: 0.33
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.09
      win_rate: 0.5
    - name: Engraved Guard
      pick_rate: 0.07
      win_rate: 0.67
  community_starters:
  - name: Bluestone Pendant
    pick_rate: 0.34
    win_rate: 0.46
  - name: Bluestone Brooch
    pick_rate: 0.22
    win_rate: 0.68
  - name: Conduit Gem
    pick_rate: 0.17
    win_rate: 0.58
  source_url: https://smitebrain.com/gods/cerberus/
  last_verified: '2026-08-15'
  god_win_rate: 0.5571428571428572
  god_matches_won: 117
  god_matches_played: 210
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-15'
  god_matches_analyzed: 4746
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Rod of Tahuti
  - Amanita Charm
  - Stampede
  flex_slots:
  - Shifter's Shield
  - Stampede
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
    this god: Freya''s Tears, Kinetic Cuirass, Amanita Charm, Rod of Tahuti, Gluttonous
    Grimoire, Shield of the Phoenix, Erosion, Oni Hunter''s Garb, Eye of Providence,
    Draconic Scale, Nimble Ring, Spectral Armor, Soul Gem, Leviathan''s Hide, Midgardian
    Mail, Mantle Of Discord, Stone of Binding, Magi''s Cloak, Helm of Radiance, Ancile,
    Screeching Gargoyle, Gladiator''s Shield, Void Shield.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.59
      win: 0.55
      pick: 0.0
      fit: 0.73
    Freya's Tears:
      total: 0.57
      efficiency: 0.59
      win: 0.6
      pick: 0.13
      fit: 0.57
    Shifter's Shield:
      total: 0.53
      efficiency: 0.52
      win: 0.54
      pick: 0.27
      fit: 0.63
    Rod of Tahuti:
      total: 0.54
      efficiency: 0.77
      win: 0.55
      pick: 0.0
      fit: 0.14
    Amanita Charm:
      total: 0.56
      efficiency: 0.63
      win: 0.55
      pick: 0.0
      fit: 0.63
    Stampede:
      total: 0.53
      efficiency: 0.48
      win: 0.65
      pick: 0.17
      fit: 0.41
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Freya's Tears
  - Rod of Tahuti
  - Amanita Charm
  - Stampede
  flex_slots:
  - Rod of Tahuti
  - Stampede
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Erosion — physical protection
    swap_item: Erosion
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Freya''s Tears,
    Soul Gem, Gluttonous Grimoire, Rod of Tahuti, Rod of Asclepius, Chandra''s Grace,
    Oni Hunter''s Garb, Erosion, Eye of Providence, Nimble Ring, Phoenix Feather,
    Spectral Armor, Draconic Scale, Leviathan''s Hide, Lifebinder, Midgardian Mail,
    Blood-Bound Book, Glorious Pridwen, Bancroft''s Talon, Ancile, Gladiator''s Shield.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.59
      win: 0.55
      pick: 0.0
      fit: 0.71
    Shield of the Phoenix:
      total: 0.58
      efficiency: 0.57
      win: 0.55
      pick: 0.0
      fit: 0.85
    Freya's Tears:
      total: 0.56
      efficiency: 0.59
      win: 0.6
      pick: 0.13
      fit: 0.5
    Rod of Tahuti:
      total: 0.54
      efficiency: 0.77
      win: 0.55
      pick: 0.0
      fit: 0.14
    Amanita Charm:
      total: 0.61
      efficiency: 0.63
      win: 0.55
      pick: 0.0
      fit: 0.91
    Stampede:
      total: 0.53
      efficiency: 0.48
      win: 0.65
      pick: 0.17
      fit: 0.43
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Screeching Gargoyle
  - Stone of Binding
  - Kinetic Cuirass
  - Freya's Tears
  - Gluttonous Grimoire
  - Rod of Tahuti
  flex_slots:
  - Stone of Binding
  - Screeching Gargoyle
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Void Shield — physical protection
    swap_item: Void Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Gluttonous Grimoire, Freya''s Tears, Kinetic Cuirass,
    Amanita Charm, Soul Gem, Stone of Binding, Screeching Gargoyle, Void Shield, The
    Cosmic Horror, Nimble Ring, Oni Hunter''s Garb, Spear of the Magus, Void Stone,
    Shield of the Phoenix, Spear of Desolation, Erosion, Spectral Armor, Eye of Providence,
    Draconic Scale, Obsidian Shard, Leviathan''s Hide, Midgardian Mail, Mantle Of
    Discord.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.52
      efficiency: 0.49
      win: 0.55
      pick: 0.0
      fit: 0.65
    Stone of Binding:
      total: 0.52
      efficiency: 0.47
      win: 0.55
      pick: 0.0
      fit: 0.72
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.59
      win: 0.55
      pick: 0.0
      fit: 0.55
    Freya's Tears:
      total: 0.54
      efficiency: 0.59
      win: 0.6
      pick: 0.13
      fit: 0.41
    Gluttonous Grimoire:
      total: 0.56
      efficiency: 0.63
      win: 0.55
      pick: 0.0
      fit: 0.61
    Rod of Tahuti:
      total: 0.58
      efficiency: 0.77
      win: 0.55
      pick: 0.0
      fit: 0.38
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Kinetic Cuirass
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Freya's Tears
  - Rod of Tahuti
  flex_slots:
  - Bracer of The Abyss
  - Bragi's Harp
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
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Nimble Ring, Freya''s Tears, Rod of Tahuti, Kinetic Cuirass, Amanita
    Charm, Gluttonous Grimoire, Oni Hunter''s Garb, Soul Gem, Shield of the Phoenix,
    Spectral Armor, Erosion, Eye of Providence, Draconic Scale, Leviathan''s Hide,
    Midgardian Mail, Helm of Radiance, Mantle Of Discord, Stone of Binding, Death
    Metal, Screeching Gargoyle, The Cosmic Horror, Yogi''s Necklace, Bracer of The
    Abyss, Ancile.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.59
      win: 0.55
      pick: 0.0
      fit: 0.46
    Bracer of The Abyss:
      total: 0.46
      efficiency: 0.51
      win: 0.55
      pick: 0.0
      fit: 0.24
    Nimble Ring:
      total: 0.53
      efficiency: 0.68
      win: 0.55
      pick: 0.0
      fit: 0.31
    Bragi's Harp:
      total: 0.46
      efficiency: 0.42
      win: 0.55
      pick: 0.0
      fit: 0.44
    Freya's Tears:
      total: 0.53
      efficiency: 0.59
      win: 0.6
      pick: 0.13
      fit: 0.33
    Rod of Tahuti:
      total: 0.53
      efficiency: 0.77
      win: 0.55
      pick: 0.0
      fit: 0.08
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Freya's Tears
  - Rod of Tahuti
  - Stampede
  flex_slots:
  - Shield of the Phoenix
  - Stampede
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Freya''s Tears, Rod of Tahuti, Kinetic
    Cuirass, Shield of the Phoenix, Amanita Charm, Soul Gem, Gluttonous Grimoire,
    Nimble Ring, Oni Hunter''s Garb, Screeching Gargoyle, Chronos'' Pendant, Chandra''s
    Grace, Spear of Desolation, Gladiator''s Shield, Erosion, Spectral Armor, Eye
    of Providence, Prophetic Cloak, Draconic Scale, Leviathan''s Hide, Helm of Radiance,
    Gem of Focus, Midgardian Mail, Mantle Of Discord.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.69
      win: 0.49
      pick: 0.29
      fit: 0.45
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.59
      win: 0.55
      pick: 0.0
      fit: 0.52
    Shield of the Phoenix:
      total: 0.53
      efficiency: 0.57
      win: 0.55
      pick: 0.0
      fit: 0.56
    Freya's Tears:
      total: 0.57
      efficiency: 0.59
      win: 0.6
      pick: 0.13
      fit: 0.59
    Rod of Tahuti:
      total: 0.54
      efficiency: 0.77
      win: 0.55
      pick: 0.0
      fit: 0.12
    Stampede:
      total: 0.51
      efficiency: 0.48
      win: 0.65
      pick: 0.17
      fit: 0.27
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Gluttonous Grimoire
  - The Crusher
  - Rod of Tahuti
  flex_slots:
  - Kinetic Cuirass
  - Gluttonous Grimoire
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Rod of Tahuti, The Crusher, Jotunn''s Revenge,
    Freya''s Tears, Kinetic Cuirass, Gluttonous Grimoire, Berserker''s Shield, Amanita
    Charm, Nimble Ring, Runeforged Hammer, Shield Splitter, Soul Gem, Hydra''s Lament,
    Oni Hunter''s Garb, Golden Blade, Shield of the Phoenix, Eye of the Storm, Pharaoh''s
    Curse, Erosion, Spectral Armor, Eye of Providence, Death Metal, The Reaper, Lernaean
    Bow, Draconic Scale, The Cosmic Horror, Avenging Blade, Damaru, Leviathan''s Hide,
    Spear of the Magus, Shogun''s Ofuda, Midgardian Mail, Mantle Of Discord, Spear
    of Desolation, Stone of Binding, Helm of Radiance, Tekko-Kagi, Tyrfing.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.64
      win: 0.55
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.59
      win: 0.55
      pick: 0.0
      fit: 0.51
    Freya's Tears:
      total: 0.54
      efficiency: 0.59
      win: 0.6
      pick: 0.13
      fit: 0.37
    Gluttonous Grimoire:
      total: 0.53
      efficiency: 0.63
      win: 0.55
      pick: 0.0
      fit: 0.42
    The Crusher:
      total: 0.54
      efficiency: 0.64
      win: 0.55
      pick: 0.0
      fit: 0.47
    Rod of Tahuti:
      total: 0.55
      efficiency: 0.77
      win: 0.55
      pick: 0.0
      fit: 0.2
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
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
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Gluttonous Grimoire,
    The Crusher, Freya''s Tears, Kinetic Cuirass, Jotunn''s Revenge, Amanita Charm,
    Berserker''s Shield, Nimble Ring, Soul Gem, Oni Hunter''s Garb, The Cosmic Horror,
    Runeforged Hammer, Shield of the Phoenix, Hydra''s Lament, Death Metal, Spear
    of the Magus, Shield Splitter, Spectral Armor, Helm of Radiance, Erosion, Spear
    of Desolation, Pharaoh''s Curse, Eye of the Storm, Golden Blade, Eye of Providence,
    Rod of Asclepius, Draconic Scale, The Reaper, Leviathan''s Hide, Obsidian Shard,
    Chronos'' Pendant, Jade Scepter, Lernaean Bow, Midgardian Mail, Shogun''s Ofuda,
    Damaru, Avenging Blade.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.64
      win: 0.55
      pick: 0.0
      fit: 0.38
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.59
      win: 0.55
      pick: 0.0
      fit: 0.49
    Freya's Tears:
      total: 0.53
      efficiency: 0.59
      win: 0.6
      pick: 0.13
      fit: 0.35
    Gluttonous Grimoire:
      total: 0.55
      efficiency: 0.63
      win: 0.55
      pick: 0.0
      fit: 0.51
    The Crusher:
      total: 0.53
      efficiency: 0.64
      win: 0.55
      pick: 0.0
      fit: 0.4
    Rod of Tahuti:
      total: 0.56
      efficiency: 0.77
      win: 0.55
      pick: 0.0
      fit: 0.3
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Rod of Tahuti
  - Amanita Charm
  - Erosion
  flex_slots:
  - Rod of Tahuti
  - Erosion
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Kinetic Cuirass, Amanita Charm, Freya''s Tears, Rod of
    Tahuti, Gluttonous Grimoire, Shield of the Phoenix, Erosion, Oni Hunter''s Garb,
    Eye of Providence, Draconic Scale, Nimble Ring, Spectral Armor, Soul Gem, Leviathan''s
    Hide, Midgardian Mail, Mantle Of Discord, Stone of Binding, Magi''s Cloak, Helm
    of Radiance, Ancile, Screeching Gargoyle, Gladiator''s Shield, Void Shield.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.69
      win: 0.49
      pick: 0.29
      fit: 0.35
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.59
      win: 0.55
      pick: 0.0
      fit: 0.73
    Freya's Tears:
      total: 0.57
      efficiency: 0.59
      win: 0.6
      pick: 0.13
      fit: 0.57
    Rod of Tahuti:
      total: 0.54
      efficiency: 0.77
      win: 0.55
      pick: 0.0
      fit: 0.14
    Amanita Charm:
      total: 0.56
      efficiency: 0.63
      win: 0.55
      pick: 0.0
      fit: 0.63
    Erosion:
      total: 0.53
      efficiency: 0.52
      win: 0.55
      pick: 0.0
      fit: 0.63
  starter: *id001
---
