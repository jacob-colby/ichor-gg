---
type: smite-build
god: Cerberus
mode: Conquest
builds:
- source: community
  aspect: Aspect of Souls
  aspect_pick_rate: 0.04
  aspect_win_rate: 0.5
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.3
    win_rate: 0.56
    alternates:
    - name: Gauntlet of Thebes
      pick_rate: 0.24
      win_rate: 0.61
    - name: Stampede
      pick_rate: 0.07
      win_rate: 0.55
  - name: Genji's Guard
    pick_rate: 0.21
    win_rate: 0.58
    alternates:
    - name: Stampede
      pick_rate: 0.14
      win_rate: 0.66
    - name: Shifter's Shield
      pick_rate: 0.13
      win_rate: 0.55
  - name: Stampede
    pick_rate: 0.09
    win_rate: 0.51
    alternates:
    - name: Genji's Guard
      pick_rate: 0.25
      win_rate: 0.62
    - name: Breastplate of Valor
      pick_rate: 0.08
      win_rate: 0.51
  - name: Shell of Rebuke
    pick_rate: 0.14
    win_rate: 0.56
    alternates:
    - name: Genji's Guard
      pick_rate: 0.1
      win_rate: 0.59
    - name: Shifter's Shield
      pick_rate: 0.07
      win_rate: 0.62
  - name: Freya's Tears
    pick_rate: 0.05
    win_rate: 0.71
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.11
      win_rate: 0.67
    - name: Spirit Robe
      pick_rate: 0.04
      win_rate: 0.71
  - name: Olmec Blue
    pick_rate: 0.05
    win_rate: 0.59
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.04
      win_rate: 0.57
    - name: Mote of Chaos
      pick_rate: 0.04
      win_rate: 0.69
  community_starters:
  - name: Bluestone Pendant
    pick_rate: 0.31
    win_rate: 0.54
  - name: Bluestone Brooch
    pick_rate: 0.23
    win_rate: 0.6
  - name: Conduit Gem
    pick_rate: 0.09
    win_rate: 0.49
  source_url: https://smitebrain.com/gods/cerberus/
  last_verified: '2026-08-08'
  god_win_rate: 0.5682539682539682
  god_matches_won: 358
  god_matches_played: 630
  god_division: obsidian
  god_window_start: '2026-07-28'
  god_window_end: '2026-08-08'
  god_matches_analyzed: 14443
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Eye of Providence
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Eye of Providence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Spirit Robe — magical protection
    swap_item: Spirit Robe
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Freya''s Tears, Amanita Charm, Kinetic Cuirass, Eye of Providence, Gluttonous
    Grimoire, Oni Hunter''s Garb, Breastplate of Valor, Shield of the Phoenix, Erosion,
    Draconic Scale, Spectral Armor, Soul Gem, Leviathan''s Hide, Yogi''s Necklace,
    Stampede, Midgardian Mail, Mantle Of Discord, Stone of Binding, Helm of Radiance,
    Hide of the Nemean Lion, Rod of Asclepius, Magi''s Cloak, Ancile, Jade Scepter,
    Gladiator''s Shield.'
  slot_scores:
    Eye of Providence:
      total: 0.54
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.63
    Genji's Guard:
      total: 0.57
      efficiency: 0.72
      win: 0.58
      pick: 0.21
      fit: 0.35
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.73
    Freya's Tears:
      total: 0.61
      efficiency: 0.59
      win: 0.71
      pick: 0.05
      fit: 0.57
    Shifter's Shield:
      total: 0.55
      efficiency: 0.55
      win: 0.56
      pick: 0.3
      fit: 0.63
    Amanita Charm:
      total: 0.55
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.63
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Shifter's Shield
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Spirit Robe — magical protection
    swap_item: Spirit Robe
  - vs_tag: physical_heavy
    swap: Eye of Providence — physical protection
    swap_item: Eye of Providence
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Freya''s Tears, Amanita Charm, Shield of the Phoenix, Kinetic Cuirass,
    Eye of Providence, Soul Gem, Gluttonous Grimoire, Rod of Asclepius, Oni Hunter''s
    Garb, Chandra''s Grace, Breastplate of Valor, Erosion, Phoenix Feather, Spectral
    Armor, Draconic Scale, Lifebinder, Blood-Bound Book, Yogi''s Necklace, Bancroft''s
    Talon, Leviathan''s Hide, Stampede, Midgardian Mail, Hide of the Nemean Lion,
    Glorious Pridwen, Jade Scepter.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.72
      win: 0.58
      pick: 0.21
      fit: 0.31
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.71
    Shield of the Phoenix:
      total: 0.55
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.85
    Freya's Tears:
      total: 0.6
      efficiency: 0.59
      win: 0.71
      pick: 0.05
      fit: 0.5
    Shifter's Shield:
      total: 0.55
      efficiency: 0.55
      win: 0.56
      pick: 0.3
      fit: 0.61
    Amanita Charm:
      total: 0.59
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.91
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Eye of Providence
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Gluttonous Grimoire
  - Shifter's Shield
  flex_slots:
  - Kinetic Cuirass
  - Eye of Providence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Stone of Binding — physical protection
    swap_item: Stone of Binding
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Freya''s Tears, Gluttonous Grimoire, Amanita Charm, Kinetic Cuirass,
    Soul Gem, Eye of Providence, Stone of Binding, Breastplate of Valor, Oni Hunter''s
    Garb, Screeching Gargoyle, Spear of the Magus, Void Shield, The Cosmic Horror,
    Void Stone, Shield of the Phoenix, Spear of Desolation, Spectral Armor, Erosion,
    Yogi''s Necklace, Obsidian Shard, Draconic Scale, Leviathan''s Hide, Helm of Radiance,
    Rod of Asclepius, Midgardian Mail.'
  slot_scores:
    Eye of Providence:
      total: 0.51
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.45
    Genji's Guard:
      total: 0.56
      efficiency: 0.72
      win: 0.58
      pick: 0.21
      fit: 0.25
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.55
    Freya's Tears:
      total: 0.59
      efficiency: 0.59
      win: 0.71
      pick: 0.05
      fit: 0.41
    Gluttonous Grimoire:
      total: 0.55
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.61
    Shifter's Shield:
      total: 0.53
      efficiency: 0.55
      win: 0.56
      pick: 0.3
      fit: 0.45
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Genji's Guard
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Freya's Tears
  - Shifter's Shield
  flex_slots:
  - Bragi's Harp
  - Nimble Ring
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Freya''s Tears, Amanita Charm, Gluttonous Grimoire, Kinetic Cuirass,
    Eye of Providence, Breastplate of Valor, Oni Hunter''s Garb, Soul Gem, Shield
    of the Phoenix, Spectral Armor, Yogi''s Necklace, Erosion, Bracer of The Abyss,
    Death Metal, Draconic Scale, Rod of Asclepius, Helm of Radiance, Leviathan''s
    Hide, Bragi''s Harp, Midgardian Mail, Hide of the Nemean Lion, Spear of the Magus,
    Jade Scepter, Mantle Of Discord, Stone of Binding.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.72
      win: 0.58
      pick: 0.21
      fit: 0.2
    Bracer of The Abyss:
      total: 0.46
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.24
    Nimble Ring:
      total: 0.44
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.31
    Bragi's Harp:
      total: 0.45
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.44
    Freya's Tears:
      total: 0.58
      efficiency: 0.59
      win: 0.71
      pick: 0.05
      fit: 0.33
    Shifter's Shield:
      total: 0.51
      efficiency: 0.55
      win: 0.56
      pick: 0.3
      fit: 0.36
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Eye of Providence — magical protection
    swap_item: Eye of Providence
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Freya''s Tears, Breastplate of Valor,
    Amanita Charm, Kinetic Cuirass, Shield of the Phoenix, Soul Gem, Gluttonous Grimoire,
    Eye of Providence, Oni Hunter''s Garb, Chronos'' Pendant, Screeching Gargoyle,
    Chandra''s Grace, Spectral Armor, Spear of Desolation, Erosion, Gladiator''s Shield,
    Yogi''s Necklace, Draconic Scale, Helm of Radiance, Rod of Asclepius, Prophetic
    Cloak, Gem of Focus, Death Metal, Leviathan''s Hide, Jade Scepter.'
  slot_scores:
    Genji's Guard:
      total: 0.59
      efficiency: 0.72
      win: 0.58
      pick: 0.21
      fit: 0.45
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.65
      win: 0.51
      pick: 0.08
      fit: 0.45
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.52
    Freya's Tears:
      total: 0.62
      efficiency: 0.59
      win: 0.71
      pick: 0.05
      fit: 0.59
    Shifter's Shield:
      total: 0.52
      efficiency: 0.55
      win: 0.56
      pick: 0.3
      fit: 0.42
    Amanita Charm:
      total: 0.52
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.42
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Freya's Tears
  - Shifter's Shield
  - The Crusher
  flex_slots:
  - The Crusher
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    win/pick). Underrated for this god: Freya''s Tears, Berserker''s Shield, The Crusher,
    Jotunn''s Revenge, Gluttonous Grimoire, Amanita Charm, Kinetic Cuirass, Eye of
    Providence, Runeforged Hammer, Hydra''s Lament, Breastplate of Valor, Oni Hunter''s
    Garb, Shield Splitter, Soul Gem, Golden Blade, Lernaean Bow, Eye of the Storm,
    Pharaoh''s Curse, Shield of the Phoenix, Death Metal, Spectral Armor, Avenging
    Blade, Erosion, Yogi''s Necklace, The Reaper, Damaru, Spear of the Magus, Draconic
    Scale, Shogun''s Ofuda, Leviathan''s Hide, The Cosmic Horror, Helm of Radiance,
    Rod of Asclepius, Dominance, Heartseeker, Riptalon, Midgardian Mail, Bragi''s
    Harp.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.72
      win: 0.58
      pick: 0.21
      fit: 0.23
    Berserker's Shield:
      total: 0.53
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.35
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.45
    Freya's Tears:
      total: 0.58
      efficiency: 0.59
      win: 0.71
      pick: 0.05
      fit: 0.37
    Shifter's Shield:
      total: 0.52
      efficiency: 0.55
      win: 0.56
      pick: 0.3
      fit: 0.41
    The Crusher:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.47
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Freya's Tears
  - Gluttonous Grimoire
  - Shifter's Shield
  - The Crusher
  flex_slots:
  - Shifter's Shield
  - The Crusher
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Freya''s Tears, Gluttonous Grimoire,
    Berserker''s Shield, Amanita Charm, The Crusher, Jotunn''s Revenge, Kinetic Cuirass,
    Soul Gem, Eye of Providence, Breastplate of Valor, Runeforged Hammer, Oni Hunter''s
    Garb, Hydra''s Lament, Death Metal, Spear of the Magus, Shield Splitter, Pharaoh''s
    Curse, The Cosmic Horror, Helm of Radiance, Rod of Asclepius, Shield of the Phoenix,
    Golden Blade, Lernaean Bow, Eye of the Storm, Spectral Armor, Yogi''s Necklace,
    Jade Scepter, Erosion, Spear of Desolation, Avenging Blade, Bragi''s Harp, Draconic
    Scale, Obsidian Shard, Damaru, The Reaper, Bracer of The Abyss, Chronos'' Pendant,
    Shogun''s Ofuda.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.72
      win: 0.58
      pick: 0.21
      fit: 0.21
    Berserker's Shield:
      total: 0.52
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.32
    Freya's Tears:
      total: 0.58
      efficiency: 0.59
      win: 0.71
      pick: 0.05
      fit: 0.35
    Gluttonous Grimoire:
      total: 0.53
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.51
    Shifter's Shield:
      total: 0.52
      efficiency: 0.55
      win: 0.56
      pick: 0.3
      fit: 0.39
    The Crusher:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.4
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Eye of Providence
  - Genji's Guard
  - Kinetic Cuirass
  - Oni Hunter's Garb
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Oni Hunter's Garb
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Kinetic Cuirass, Eye of Providence, Gluttonous
    Grimoire, Freya''s Tears, Oni Hunter''s Garb, Breastplate of Valor, Shield of
    the Phoenix, Erosion, Draconic Scale, Spectral Armor, Soul Gem, Leviathan''s Hide,
    Yogi''s Necklace, Midgardian Mail, Mantle Of Discord, Stone of Binding, Helm of
    Radiance, Hide of the Nemean Lion, Rod of Asclepius, Magi''s Cloak, Stampede,
    Ancile, Jade Scepter, Gladiator''s Shield.'
  slot_scores:
    Eye of Providence:
      total: 0.54
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.63
    Genji's Guard:
      total: 0.57
      efficiency: 0.72
      win: 0.58
      pick: 0.21
      fit: 0.35
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.73
    Oni Hunter's Garb:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.41
    Freya's Tears:
      total: 0.61
      efficiency: 0.59
      win: 0.71
      pick: 0.05
      fit: 0.57
    Amanita Charm:
      total: 0.55
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.63
  starter: *id001
---
