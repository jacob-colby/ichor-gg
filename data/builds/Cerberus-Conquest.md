---
type: smite-build
god: Cerberus
mode: Conquest
builds:
- source: community
  aspect: Aspect of Souls
  aspect_pick_rate: 0.05
  aspect_win_rate: 0.38
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.27
    win_rate: 0.53
    alternates:
    - name: Gauntlet of Thebes
      pick_rate: 0.24
      win_rate: 0.58
    - name: Stampede
      pick_rate: 0.11
      win_rate: 0.35
  - name: Genji's Guard
    pick_rate: 0.23
    win_rate: 0.44
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.13
      win_rate: 0.46
    - name: Shifter's Shield
      pick_rate: 0.13
      win_rate: 0.54
  - name: Shell of Rebuke
    pick_rate: 0.13
    win_rate: 0.54
    alternates:
    - name: Genji's Guard
      pick_rate: 0.15
      win_rate: 0.55
    - name: Stampede
      pick_rate: 0.1
      win_rate: 0.64
  - name: Freya's Tears
    pick_rate: 0.08
    win_rate: 0.52
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.14
      win_rate: 0.54
    - name: Genji's Guard
      pick_rate: 0.09
      win_rate: 0.5
  - name: Hide of the Nemean Lion
    pick_rate: 0.07
    win_rate: 0.53
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.08
      win_rate: 0.78
    - name: Freya's Tears
      pick_rate: 0.08
      win_rate: 0.71
  - name: Engraved Guard
    pick_rate: 0.08
    win_rate: 0.55
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.07
      win_rate: 0.44
    - name: Captain's Ring
      pick_rate: 0.05
      win_rate: 0.43
  community_starters:
  - name: Bluestone Pendant
    pick_rate: 0.35
    win_rate: 0.44
  - name: Bluestone Brooch
    pick_rate: 0.23
    win_rate: 0.68
  - name: Conduit Gem
    pick_rate: 0.15
    win_rate: 0.5
  source_url: https://smitebrain.com/gods/cerberus/
  last_verified: '2026-08-16'
  god_win_rate: 0.528169014084507
  god_matches_won: 150
  god_matches_played: 284
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-16'
  god_matches_analyzed: 6103
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  - Erosion
  - Stampede
  flex_slots:
  - Stampede
  - Erosion
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Oni Hunter's Garb — magical protection
    swap_item: Oni Hunter's Garb
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Kinetic Cuirass, Amanita Charm, Freya''s Tears, Rod of Tahuti, Gluttonous
    Grimoire, Shield of the Phoenix, Erosion, Oni Hunter''s Garb, Eye of Providence,
    Draconic Scale, Nimble Ring, Spectral Armor, Soul Gem, Leviathan''s Hide, Midgardian
    Mail, Mantle Of Discord, Stone of Binding, Magi''s Cloak, Helm of Radiance, Ancile,
    Screeching Gargoyle, Gladiator''s Shield, Void Shield.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.59
      win: 0.53
      pick: 0.0
      fit: 0.73
    Freya's Tears:
      total: 0.53
      efficiency: 0.59
      win: 0.52
      pick: 0.13
      fit: 0.57
    Shifter's Shield:
      total: 0.53
      efficiency: 0.52
      win: 0.53
      pick: 0.27
      fit: 0.63
    Amanita Charm:
      total: 0.55
      efficiency: 0.63
      win: 0.53
      pick: 0.0
      fit: 0.63
    Erosion:
      total: 0.51
      efficiency: 0.52
      win: 0.53
      pick: 0.0
      fit: 0.63
    Stampede:
      total: 0.52
      efficiency: 0.48
      win: 0.64
      pick: 0.16
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
  - Shifter's Shield
  - Amanita Charm
  - Stampede
  flex_slots:
  - Shifter's Shield
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Oni Hunter's Garb — magical protection
    swap_item: Oni Hunter's Garb
  - vs_tag: physical_heavy
    swap: Erosion — physical protection
    swap_item: Erosion
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Soul Gem, Gluttonous
    Grimoire, Rod of Tahuti, Rod of Asclepius, Chandra''s Grace, Freya''s Tears, Oni
    Hunter''s Garb, Erosion, Eye of Providence, Nimble Ring, Phoenix Feather, Spectral
    Armor, Draconic Scale, Leviathan''s Hide, Lifebinder, Midgardian Mail, Blood-Bound
    Book, Glorious Pridwen, Bancroft''s Talon, Ancile, Gladiator''s Shield.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.59
      win: 0.53
      pick: 0.0
      fit: 0.71
    Shield of the Phoenix:
      total: 0.56
      efficiency: 0.57
      win: 0.53
      pick: 0.0
      fit: 0.85
    Freya's Tears:
      total: 0.52
      efficiency: 0.59
      win: 0.52
      pick: 0.13
      fit: 0.5
    Shifter's Shield:
      total: 0.53
      efficiency: 0.52
      win: 0.53
      pick: 0.27
      fit: 0.61
    Amanita Charm:
      total: 0.6
      efficiency: 0.63
      win: 0.53
      pick: 0.0
      fit: 0.91
    Stampede:
      total: 0.53
      efficiency: 0.48
      win: 0.64
      pick: 0.16
      fit: 0.43
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Screeching Gargoyle
  - Stone of Binding
  - Kinetic Cuirass
  - Gluttonous Grimoire
  - Rod of Tahuti
  - Stampede
  flex_slots:
  - Stampede
  - Screeching Gargoyle
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Gluttonous Grimoire, Kinetic Cuirass, Amanita Charm,
    Soul Gem, Stone of Binding, Screeching Gargoyle, Freya''s Tears, Void Shield,
    The Cosmic Horror, Nimble Ring, Oni Hunter''s Garb, Spear of the Magus, Void Stone,
    Shield of the Phoenix, Spear of Desolation, Erosion, Spectral Armor, Eye of Providence,
    Draconic Scale, Obsidian Shard, Leviathan''s Hide, Midgardian Mail, Mantle Of
    Discord.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.51
      efficiency: 0.49
      win: 0.53
      pick: 0.0
      fit: 0.65
    Stone of Binding:
      total: 0.51
      efficiency: 0.47
      win: 0.53
      pick: 0.0
      fit: 0.72
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.59
      win: 0.53
      pick: 0.0
      fit: 0.55
    Gluttonous Grimoire:
      total: 0.55
      efficiency: 0.63
      win: 0.53
      pick: 0.0
      fit: 0.61
    Rod of Tahuti:
      total: 0.56
      efficiency: 0.77
      win: 0.53
      pick: 0.0
      fit: 0.38
    Stampede:
      total: 0.51
      efficiency: 0.48
      win: 0.64
      pick: 0.16
      fit: 0.29
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Kinetic Cuirass
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Amanita Charm
  - Stampede
  flex_slots:
  - Bracer of The Abyss
  - Bragi's Harp
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Nimble Ring, Rod of Tahuti, Kinetic Cuirass, Amanita Charm, Gluttonous
    Grimoire, Freya''s Tears, Oni Hunter''s Garb, Soul Gem, Shield of the Phoenix,
    Spectral Armor, Erosion, Eye of Providence, Draconic Scale, Leviathan''s Hide,
    Midgardian Mail, Helm of Radiance, Mantle Of Discord, Stone of Binding, Death
    Metal, Screeching Gargoyle, The Cosmic Horror, Yogi''s Necklace, Bracer of The
    Abyss, Ancile.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.59
      win: 0.53
      pick: 0.0
      fit: 0.46
    Bracer of The Abyss:
      total: 0.45
      efficiency: 0.51
      win: 0.53
      pick: 0.0
      fit: 0.24
    Nimble Ring:
      total: 0.52
      efficiency: 0.68
      win: 0.53
      pick: 0.0
      fit: 0.31
    Bragi's Harp:
      total: 0.45
      efficiency: 0.42
      win: 0.53
      pick: 0.0
      fit: 0.44
    Amanita Charm:
      total: 0.51
      efficiency: 0.63
      win: 0.53
      pick: 0.0
      fit: 0.36
    Stampede:
      total: 0.5
      efficiency: 0.48
      win: 0.64
      pick: 0.16
      fit: 0.23
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Freya's Tears
  - Stampede
  flex_slots:
  - Breastplate of Valor
  - Stampede
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
      total: 0.52
      efficiency: 0.69
      win: 0.44
      pick: 0.31
      fit: 0.45
    Breastplate of Valor:
      total: 0.51
      efficiency: 0.64
      win: 0.46
      pick: 0.18
      fit: 0.45
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.59
      win: 0.53
      pick: 0.0
      fit: 0.52
    Shield of the Phoenix:
      total: 0.52
      efficiency: 0.57
      win: 0.53
      pick: 0.0
      fit: 0.56
    Freya's Tears:
      total: 0.53
      efficiency: 0.59
      win: 0.52
      pick: 0.13
      fit: 0.59
    Stampede:
      total: 0.5
      efficiency: 0.48
      win: 0.64
      pick: 0.16
      fit: 0.27
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Gluttonous Grimoire
  - The Crusher
  - Stampede
  flex_slots:
  - Berserker's Shield
  - Stampede
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
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
    win/pick). Underrated for this god: Rod of Tahuti, The Crusher, Jotunn''s Revenge,
    Kinetic Cuirass, Gluttonous Grimoire, Berserker''s Shield, Amanita Charm, Freya''s
    Tears, Nimble Ring, Runeforged Hammer, Shield Splitter, Soul Gem, Hydra''s Lament,
    Oni Hunter''s Garb, Golden Blade, Shield of the Phoenix, Eye of the Storm, Pharaoh''s
    Curse, Erosion, Spectral Armor, Eye of Providence, Death Metal, The Reaper, Lernaean
    Bow, Draconic Scale, The Cosmic Horror, Avenging Blade, Damaru, Leviathan''s Hide,
    Spear of the Magus, Shogun''s Ofuda, Midgardian Mail, Mantle Of Discord, Spear
    of Desolation, Stone of Binding, Helm of Radiance, Tekko-Kagi, Tyrfing.'
  slot_scores:
    Berserker's Shield:
      total: 0.52
      efficiency: 0.66
      win: 0.53
      pick: 0.0
      fit: 0.35
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
      fit: 0.51
    Gluttonous Grimoire:
      total: 0.52
      efficiency: 0.63
      win: 0.53
      pick: 0.0
      fit: 0.42
    The Crusher:
      total: 0.53
      efficiency: 0.64
      win: 0.53
      pick: 0.0
      fit: 0.47
    Stampede:
      total: 0.5
      efficiency: 0.48
      win: 0.64
      pick: 0.16
      fit: 0.27
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Gluttonous Grimoire
  - The Crusher
  - Stampede
  flex_slots:
  - Berserker's Shield
  - Stampede
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
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
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Gluttonous Grimoire,
    The Crusher, Kinetic Cuirass, Jotunn''s Revenge, Amanita Charm, Berserker''s Shield,
    Nimble Ring, Soul Gem, Freya''s Tears, Oni Hunter''s Garb, The Cosmic Horror,
    Runeforged Hammer, Shield of the Phoenix, Hydra''s Lament, Death Metal, Spear
    of the Magus, Shield Splitter, Spectral Armor, Helm of Radiance, Erosion, Spear
    of Desolation, Pharaoh''s Curse, Eye of the Storm, Golden Blade, Eye of Providence,
    Rod of Asclepius, Draconic Scale, The Reaper, Leviathan''s Hide, Obsidian Shard,
    Chronos'' Pendant, Jade Scepter, Lernaean Bow, Midgardian Mail, Shogun''s Ofuda,
    Damaru, Avenging Blade.'
  slot_scores:
    Berserker's Shield:
      total: 0.52
      efficiency: 0.66
      win: 0.53
      pick: 0.0
      fit: 0.32
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.64
      win: 0.53
      pick: 0.0
      fit: 0.38
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.59
      win: 0.53
      pick: 0.0
      fit: 0.49
    Gluttonous Grimoire:
      total: 0.54
      efficiency: 0.63
      win: 0.53
      pick: 0.0
      fit: 0.51
    The Crusher:
      total: 0.52
      efficiency: 0.64
      win: 0.53
      pick: 0.0
      fit: 0.4
    Stampede:
      total: 0.5
      efficiency: 0.48
      win: 0.64
      pick: 0.16
      fit: 0.25
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  - Erosion
  flex_slots:
  - Erosion
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Oni Hunter's Garb — magical protection
    swap_item: Oni Hunter's Garb
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
      total: 0.51
      efficiency: 0.69
      win: 0.44
      pick: 0.31
      fit: 0.35
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.59
      win: 0.53
      pick: 0.0
      fit: 0.73
    Freya's Tears:
      total: 0.53
      efficiency: 0.59
      win: 0.52
      pick: 0.13
      fit: 0.57
    Shifter's Shield:
      total: 0.53
      efficiency: 0.52
      win: 0.53
      pick: 0.27
      fit: 0.63
    Amanita Charm:
      total: 0.55
      efficiency: 0.63
      win: 0.53
      pick: 0.0
      fit: 0.63
    Erosion:
      total: 0.51
      efficiency: 0.52
      win: 0.53
      pick: 0.0
      fit: 0.63
  starter: *id001
---
