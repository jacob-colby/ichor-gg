---
type: smite-build
god: Khepri
mode: Conquest
builds:
- source: community
  aspect: Aspect of Laceration
  aspect_pick_rate: 0.7
  aspect_win_rate: 0.57
  slot_order:
  - name: Gauntlet of Thebes
    pick_rate: 0.27
    win_rate: 0.53
    alternates:
    - name: Yogi's Necklace
      pick_rate: 0.15
      win_rate: 0.44
    - name: Shifter's Shield
      pick_rate: 0.13
      win_rate: 0.73
  - name: Genji's Guard
    pick_rate: 0.23
    win_rate: 0.46
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.09
      win_rate: 0.33
    - name: Prophetic Cloak
      pick_rate: 0.09
      win_rate: 0.53
  - name: Breastplate of Valor
    pick_rate: 0.16
    win_rate: 0.65
    alternates:
    - name: Genji's Guard
      pick_rate: 0.15
      win_rate: 0.56
    - name: Stampede
      pick_rate: 0.07
      win_rate: 0.42
  - name: Shell of Rebuke
    pick_rate: 0.08
    win_rate: 0.33
    alternates:
    - name: Genji's Guard
      pick_rate: 0.1
      win_rate: 0.69
    - name: Breastplate of Valor
      pick_rate: 0.08
      win_rate: 0.62
  - name: Stampede
    pick_rate: 0.05
    win_rate: 0.71
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.07
      win_rate: 0.89
    - name: Legionnaire Armor
      pick_rate: 0.05
      win_rate: 0.57
  - name: Medal of Disruption
    pick_rate: 0.08
    win_rate: 0.43
    alternates:
    - name: Olmec Blue
      pick_rate: 0.06
      win_rate: 0.6
    - name: Engraved Guard
      pick_rate: 0.06
      win_rate: 0.6
  source_url: https://smitebrain.com/gods/khepri/
  last_verified: '2026-08-01'
  god_win_rate: 0.5207100591715976
  god_matches_won: 88
  god_matches_played: 169
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
  - Eye of Providence
  - Breastplate of Valor
  - Kinetic Cuirass
  - Shifter's Shield
  - Amanita Charm
  - Stampede
  flex_slots:
  - Kinetic Cuirass
  - Eye of Providence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Shifter''s Shield, Stampede, Amanita Charm, Kinetic Cuirass, Eye of
    Providence, Freya''s Tears, Gluttonous Grimoire, Oni Hunter''s Garb, Shield of
    the Phoenix, Erosion, Draconic Scale, Spectral Armor, Soul Gem, Prophetic Cloak,
    Leviathan''s Hide, Mantle Of Discord, Stone of Binding, Midgardian Mail, Hide
    of the Nemean Lion, Helm of Radiance, Rod of Asclepius, Magi''s Cloak, Gladiator''s
    Shield, Ancile, Yogi''s Necklace.'
  slot_scores:
    Eye of Providence:
      total: 0.55
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.7
    Breastplate of Valor:
      total: 0.59
      efficiency: 0.65
      win: 0.65
      pick: 0.16
      fit: 0.4
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.8
    Shifter's Shield:
      total: 0.63
      efficiency: 0.55
      win: 0.73
      pick: 0.13
      fit: 0.7
    Amanita Charm:
      total: 0.56
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.7
    Stampede:
      total: 0.57
      efficiency: 0.52
      win: 0.71
      pick: 0.05
      fit: 0.45
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Breastplate of Valor
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Shifter's Shield
  - Amanita Charm
  - Stampede
  flex_slots:
  - Shield of the Phoenix
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Eye of Providence — magical protection
    swap_item: Eye of Providence
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Shifter''s Shield, Amanita Charm, Shield of the Phoenix, Kinetic Cuirass,
    Eye of Providence, Soul Gem, Gluttonous Grimoire, Rod of Asclepius, Oni Hunter''s
    Garb, Chandra''s Grace, Freya''s Tears, Erosion, Draconic Scale, Phoenix Feather,
    Spectral Armor, Lifebinder, Leviathan''s Hide, Blood-Bound Book, Bancroft''s Talon,
    Midgardian Mail, Glorious Pridwen, Hide of the Nemean Lion, Gladiator''s Shield,
    Jade Scepter, Yogi''s Necklace.'
  slot_scores:
    Breastplate of Valor:
      total: 0.58
      efficiency: 0.65
      win: 0.65
      pick: 0.16
      fit: 0.37
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.78
    Shield of the Phoenix:
      total: 0.56
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.93
    Shifter's Shield:
      total: 0.63
      efficiency: 0.55
      win: 0.73
      pick: 0.13
      fit: 0.68
    Amanita Charm:
      total: 0.6
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.98
    Stampede:
      total: 0.57
      efficiency: 0.52
      win: 0.71
      pick: 0.05
      fit: 0.47
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Eye of Providence
  - Breastplate of Valor
  - Kinetic Cuirass
  - Gluttonous Grimoire
  - Shifter's Shield
  - Stampede
  flex_slots:
  - Kinetic Cuirass
  - Eye of Providence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
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
    for this god: Shifter''s Shield, Gluttonous Grimoire, Amanita Charm, Kinetic Cuirass,
    Soul Gem, Eye of Providence, Stone of Binding, Oni Hunter''s Garb, Freya''s Tears,
    Screeching Gargoyle, Spear of the Magus, Void Shield, The Cosmic Horror, Shield
    of the Phoenix, Spear of Desolation, Void Stone, Erosion, Spectral Armor, Obsidian
    Shard, Draconic Scale, Leviathan''s Hide, Helm of Radiance, Rod of Asclepius,
    Midgardian Mail, Yogi''s Necklace.'
  slot_scores:
    Eye of Providence:
      total: 0.51
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.49
    Breastplate of Valor:
      total: 0.57
      efficiency: 0.65
      win: 0.65
      pick: 0.16
      fit: 0.28
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.59
    Gluttonous Grimoire:
      total: 0.55
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.65
    Shifter's Shield:
      total: 0.6
      efficiency: 0.55
      win: 0.73
      pick: 0.13
      fit: 0.49
    Stampede:
      total: 0.55
      efficiency: 0.52
      win: 0.71
      pick: 0.05
      fit: 0.31
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Breastplate of Valor
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Shifter's Shield
  - Stampede
  flex_slots:
  - Bragi's Harp
  - Nimble Ring
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
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
    this god: Shifter''s Shield, Amanita Charm, Gluttonous Grimoire, Kinetic Cuirass,
    Eye of Providence, Oni Hunter''s Garb, Freya''s Tears, Soul Gem, Shield of the
    Phoenix, Spectral Armor, Erosion, Bracer of The Abyss, Death Metal, Draconic Scale,
    Rod of Asclepius, Helm of Radiance, Leviathan''s Hide, Bragi''s Harp, Midgardian
    Mail, Spear of the Magus, Hide of the Nemean Lion, Yogi''s Necklace, Jade Scepter,
    Mantle Of Discord, Stone of Binding.'
  slot_scores:
    Breastplate of Valor:
      total: 0.56
      efficiency: 0.65
      win: 0.65
      pick: 0.16
      fit: 0.21
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
      fit: 0.3
    Bragi's Harp:
      total: 0.45
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.44
    Shifter's Shield:
      total: 0.58
      efficiency: 0.55
      win: 0.73
      pick: 0.13
      fit: 0.36
    Stampede:
      total: 0.54
      efficiency: 0.52
      win: 0.71
      pick: 0.05
      fit: 0.23
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  - Stampede
  flex_slots:
  - Freya's Tears
  - Amanita Charm
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
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
    + fit + win/pick). Underrated for this god: Shifter''s Shield, Freya''s Tears,
    Amanita Charm, Kinetic Cuirass, Shield of the Phoenix, Soul Gem, Gluttonous Grimoire,
    Eye of Providence, Oni Hunter''s Garb, Prophetic Cloak, Chronos'' Pendant, Screeching
    Gargoyle, Chandra''s Grace, Spear of Desolation, Gladiator''s Shield, Spectral
    Armor, Erosion, Draconic Scale, Helm of Radiance, Rod of Asclepius, Gem of Focus,
    Death Metal, Leviathan''s Hide, Jade Scepter, Yogi''s Necklace.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.72
      win: 0.46
      pick: 0.23
      fit: 0.48
    Breastplate of Valor:
      total: 0.6
      efficiency: 0.65
      win: 0.65
      pick: 0.16
      fit: 0.48
    Freya's Tears:
      total: 0.53
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.64
    Shifter's Shield:
      total: 0.6
      efficiency: 0.55
      win: 0.73
      pick: 0.13
      fit: 0.45
    Amanita Charm:
      total: 0.52
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.45
    Stampede:
      total: 0.55
      efficiency: 0.52
      win: 0.71
      pick: 0.05
      fit: 0.29
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Shifter's Shield
  - The Crusher
  - Stampede
  flex_slots:
  - Jotunn's Revenge
  - The Crusher
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
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
    win/pick). Underrated for this god: Shifter''s Shield, Berserker''s Shield, Jotunn''s
    Revenge, The Crusher, Gluttonous Grimoire, Amanita Charm, Kinetic Cuirass, Eye
    of Providence, Runeforged Hammer, Hydra''s Lament, Oni Hunter''s Garb, Soul Gem,
    Shield Splitter, Freya''s Tears, Golden Blade, Lernaean Bow, Eye of the Storm,
    Pharaoh''s Curse, Shield of the Phoenix, Death Metal, Spectral Armor, Avenging
    Blade, Erosion, The Reaper, Damaru, Spear of the Magus, Draconic Scale, Shogun''s
    Ofuda, Leviathan''s Hide, The Cosmic Horror, Helm of Radiance, Rod of Asclepius,
    Dominance, Heartseeker, Riptalon, Midgardian Mail, Bragi''s Harp, Yogi''s Necklace.'
  slot_scores:
    Berserker's Shield:
      total: 0.53
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.35
    Breastplate of Valor:
      total: 0.56
      efficiency: 0.65
      win: 0.65
      pick: 0.16
      fit: 0.23
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.45
    Shifter's Shield:
      total: 0.59
      efficiency: 0.55
      win: 0.73
      pick: 0.13
      fit: 0.41
    The Crusher:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.46
    Stampede:
      total: 0.54
      efficiency: 0.52
      win: 0.71
      pick: 0.05
      fit: 0.26
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Breastplate of Valor
  - Jotunn's Revenge
  - Gluttonous Grimoire
  - Shifter's Shield
  - The Crusher
  - Stampede
  flex_slots:
  - Jotunn's Revenge
  - The Crusher
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Shifter''s Shield, Gluttonous Grimoire,
    Amanita Charm, Jotunn''s Revenge, The Crusher, Berserker''s Shield, Kinetic Cuirass,
    Soul Gem, Eye of Providence, Runeforged Hammer, Oni Hunter''s Garb, Hydra''s Lament,
    Freya''s Tears, Death Metal, Spear of the Magus, Shield Splitter, Shield of the
    Phoenix, The Cosmic Horror, Helm of Radiance, Rod of Asclepius, Eye of the Storm,
    Spectral Armor, Spear of Desolation, Erosion, Jade Scepter, Pharaoh''s Curse,
    Avenging Blade, Draconic Scale, Golden Blade, Obsidian Shard, Chronos'' Pendant,
    Lernaean Bow, The Reaper, Triton''s Conch, Damaru, Leviathan''s Hide, Wish-Granting
    Pearl, Yogi''s Necklace.'
  slot_scores:
    Breastplate of Valor:
      total: 0.56
      efficiency: 0.65
      win: 0.65
      pick: 0.16
      fit: 0.24
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.41
    Gluttonous Grimoire:
      total: 0.54
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.54
    Shifter's Shield:
      total: 0.59
      efficiency: 0.55
      win: 0.73
      pick: 0.13
      fit: 0.41
    The Crusher:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.42
    Stampede:
      total: 0.54
      efficiency: 0.52
      win: 0.71
      pick: 0.05
      fit: 0.26
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Eye of Providence
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Freya's Tears
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
    Underrated for this god: Amanita Charm, Kinetic Cuirass, Eye of Providence, Freya''s
    Tears, Gluttonous Grimoire, Shifter''s Shield, Oni Hunter''s Garb, Shield of the
    Phoenix, Erosion, Draconic Scale, Spectral Armor, Soul Gem, Leviathan''s Hide,
    Mantle Of Discord, Stone of Binding, Midgardian Mail, Yogi''s Necklace, Hide of
    the Nemean Lion, Helm of Radiance, Rod of Asclepius, Magi''s Cloak, Gladiator''s
    Shield, Stampede, Ancile, Prophetic Cloak.'
  slot_scores:
    Eye of Providence:
      total: 0.55
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.7
    Genji's Guard:
      total: 0.53
      efficiency: 0.72
      win: 0.46
      pick: 0.23
      fit: 0.4
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.8
    Freya's Tears:
      total: 0.53
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.65
    Shifter's Shield:
      total: 0.63
      efficiency: 0.55
      win: 0.73
      pick: 0.13
      fit: 0.7
    Amanita Charm:
      total: 0.56
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.7
  starter: *id001
---
