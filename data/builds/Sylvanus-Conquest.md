---
type: smite-build
god: Sylvanus
mode: Conquest
builds:
- source: community
  aspect: Aspect of Grover's Wrath
  aspect_pick_rate: 0.23
  aspect_win_rate: 0.54
  slot_order:
  - name: Tyrfing
    pick_rate: 0.2
    win_rate: 0.55
    alternates:
    - name: Prophetic Cloak
      pick_rate: 0.12
      win_rate: 0.48
    - name: Gauntlet of Thebes
      pick_rate: 0.12
      win_rate: 0.5
  - name: Genji's Guard
    pick_rate: 0.19
    win_rate: 0.47
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.1
      win_rate: 0.47
    - name: Bragi's Harp
      pick_rate: 0.1
      win_rate: 0.5
  - name: Breastplate of Valor
    pick_rate: 0.17
    win_rate: 0.48
    alternates:
    - name: Genji's Guard
      pick_rate: 0.16
      win_rate: 0.48
    - name: Circe's Hexstone
      pick_rate: 0.05
      win_rate: 0.57
  - name: Shell of Rebuke
    pick_rate: 0.1
    win_rate: 0.49
    alternates:
    - name: Genji's Guard
      pick_rate: 0.08
      win_rate: 0.56
    - name: Shield of the Phoenix
      pick_rate: 0.07
      win_rate: 0.53
  - name: Dwarven Plate
    pick_rate: 0.04
    win_rate: 0.53
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.07
      win_rate: 0.67
    - name: Engraved Guard
      pick_rate: 0.04
      win_rate: 0.46
  - name: Engraved Guard
    pick_rate: 0.08
    win_rate: 0.57
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.04
      win_rate: 0.57
    - name: Legionnaire Armor
      pick_rate: 0.04
      win_rate: 0.52
  community_starters:
  - name: Selflessness
    pick_rate: 0.29
    win_rate: 0.47
  - name: Death's Embrace
    pick_rate: 0.14
    win_rate: 0.54
  - name: Heroism
    pick_rate: 0.14
    win_rate: 0.58
  source_url: https://smitebrain.com/gods/sylvanus/
  last_verified: '2026-08-07'
  god_win_rate: 0.5059252506836828
  god_matches_won: 555
  god_matches_played: 1097
  god_division: obsidian
  god_window_start: '2026-07-28'
  god_window_end: '2026-08-07'
  god_matches_analyzed: 13100
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
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
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Kinetic Cuirass, Eye of Providence, Shield of the Phoenix,
    Gluttonous Grimoire, Freya''s Tears, Oni Hunter''s Garb, Shifter''s Shield, Erosion,
    Soul Gem, Draconic Scale, Spectral Armor, Helm of Radiance, Rod of Asclepius,
    Leviathan''s Hide, Yogi''s Necklace, Midgardian Mail, Mantle Of Discord, Stone
    of Binding, Hide of the Nemean Lion, Jade Scepter, Gladiator''s Shield, Screeching
    Gargoyle, Chronos'' Pendant, Magi''s Cloak.'
  slot_scores:
    Eye of Providence:
      total: 0.54
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.63
    Genji's Guard:
      total: 0.53
      efficiency: 0.72
      win: 0.47
      pick: 0.19
      fit: 0.39
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
      total: 0.52
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.62
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
  - Eye of Providence
  - Genji's Guard
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Oni Hunter's Garb
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Oni Hunter's Garb
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Soul Gem, Kinetic Cuirass, Gluttonous
    Grimoire, Rod of Asclepius, Eye of Providence, Chandra''s Grace, Oni Hunter''s
    Garb, Freya''s Tears, Shifter''s Shield, Lifebinder, Erosion, Blood-Bound Book,
    Phoenix Feather, Spectral Armor, Bancroft''s Talon, Draconic Scale, Yogi''s Necklace,
    Leviathan''s Hide, Jade Scepter, Glorious Pridwen, Helm of Radiance, Midgardian
    Mail, Hide of the Nemean Lion.'
  slot_scores:
    Eye of Providence:
      total: 0.53
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.62
    Genji's Guard:
      total: 0.53
      efficiency: 0.72
      win: 0.47
      pick: 0.19
      fit: 0.36
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.72
    Shield of the Phoenix:
      total: 0.58
      efficiency: 0.57
      win: 0.53
      pick: 0.07
      fit: 0.9
    Oni Hunter's Garb:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.43
    Amanita Charm:
      total: 0.59
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.92
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Eye of Providence
  - Genji's Guard
  - Kinetic Cuirass
  - Gluttonous Grimoire
  - Spear of the Magus
  flex_slots:
  - Stone of Binding
  - Spear of the Magus
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Gluttonous Grimoire, Soul Gem, Amanita Charm, Kinetic Cuirass, Eye
    of Providence, Shield of the Phoenix, Stone of Binding, Spear of the Magus, Screeching
    Gargoyle, Oni Hunter''s Garb, Freya''s Tears, The Cosmic Horror, Void Shield,
    Spear of Desolation, Shifter''s Shield, Void Stone, Obsidian Shard, Spectral Armor,
    Erosion, Yogi''s Necklace, Draconic Scale, Helm of Radiance, Rod of Asclepius,
    Leviathan''s Hide, Dreamer''s Idol.'
  slot_scores:
    Stone of Binding:
      total: 0.5
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.72
    Eye of Providence:
      total: 0.51
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.45
    Genji's Guard:
      total: 0.51
      efficiency: 0.72
      win: 0.47
      pick: 0.19
      fit: 0.28
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.55
    Gluttonous Grimoire:
      total: 0.55
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.66
    Spear of the Magus:
      total: 0.5
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.43
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Gluttonous Grimoire
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
    swap: Eye of Providence — physical protection
    swap_item: Eye of Providence
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Gluttonous Grimoire, Amanita Charm, Kinetic Cuirass, Eye of Providence,
    Shield of the Phoenix, Oni Hunter''s Garb, Soul Gem, Freya''s Tears, Shifter''s
    Shield, Yogi''s Necklace, Spectral Armor, Bracer of The Abyss, Death Metal, Erosion,
    Rod of Asclepius, Bragi''s Harp, Helm of Radiance, Draconic Scale, Spear of the
    Magus, Leviathan''s Hide, Jade Scepter, Blood-Bound Book, Bancroft''s Talon, Midgardian
    Mail, Chronos'' Pendant.'
  slot_scores:
    Genji's Guard:
      total: 0.5
      efficiency: 0.72
      win: 0.47
      pick: 0.19
      fit: 0.21
    Kinetic Cuirass:
      total: 0.5
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.44
    Bracer of The Abyss:
      total: 0.46
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.26
    Nimble Ring:
      total: 0.44
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.32
    Bragi's Harp:
      total: 0.46
      efficiency: 0.46
      win: 0.5
      pick: 0.1
      fit: 0.46
    Gluttonous Grimoire:
      total: 0.51
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.37
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Eye of Providence
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Freya's Tears
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
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Shield of the Phoenix, Freya''s Tears,
    Amanita Charm, Kinetic Cuirass, Soul Gem, Gluttonous Grimoire, Eye of Providence,
    Oni Hunter''s Garb, Shifter''s Shield, Chronos'' Pendant, Screeching Gargoyle,
    Chandra''s Grace, Spear of Desolation, Gladiator''s Shield, Spectral Armor, Erosion,
    Yogi''s Necklace, Draconic Scale, Prophetic Cloak, Helm of Radiance, Rod of Asclepius,
    Gem of Focus, Death Metal, Leviathan''s Hide, Jade Scepter.'
  slot_scores:
    Eye of Providence:
      total: 0.51
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.45
    Genji's Guard:
      total: 0.54
      efficiency: 0.72
      win: 0.47
      pick: 0.19
      fit: 0.48
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.65
      win: 0.48
      pick: 0.17
      fit: 0.48
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.55
    Shield of the Phoenix:
      total: 0.53
      efficiency: 0.57
      win: 0.53
      pick: 0.07
      fit: 0.61
    Freya's Tears:
      total: 0.53
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.64
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Gluttonous Grimoire
  - The Crusher
  flex_slots:
  - Kinetic Cuirass
  - Genji's Guard
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Berserker''s Shield, Gluttonous Grimoire,
    Jotunn''s Revenge, The Crusher, Amanita Charm, Kinetic Cuirass, Eye of Providence,
    Hydra''s Lament, Runeforged Hammer, Soul Gem, Shield of the Phoenix, Oni Hunter''s
    Garb, Freya''s Tears, Shield Splitter, Golden Blade, Death Metal, Lernaean Bow,
    Pharaoh''s Curse, Shifter''s Shield, Eye of the Storm, Spear of the Magus, Spectral
    Armor, Yogi''s Necklace, Avenging Blade, Erosion, Damaru, The Reaper, The Cosmic
    Horror, Helm of Radiance, Rod of Asclepius, Bragi''s Harp, Draconic Scale, Shogun''s
    Ofuda, Spear of Desolation, Leviathan''s Hide, Dominance, Jade Scepter, Riptalon.'
  slot_scores:
    Genji's Guard:
      total: 0.51
      efficiency: 0.72
      win: 0.47
      pick: 0.19
      fit: 0.24
    Berserker's Shield:
      total: 0.52
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.33
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.48
    Gluttonous Grimoire:
      total: 0.52
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.44
    The Crusher:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.44
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Gluttonous Grimoire
  - The Crusher
  flex_slots:
  - Kinetic Cuirass
  - Genji's Guard
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Gluttonous Grimoire, Jotunn''s Revenge,
    Amanita Charm, The Crusher, Berserker''s Shield, Kinetic Cuirass, Soul Gem, Eye
    of Providence, Shield of the Phoenix, Hydra''s Lament, Runeforged Hammer, Oni
    Hunter''s Garb, Freya''s Tears, Death Metal, Spear of the Magus, Shield Splitter,
    Shifter''s Shield, The Cosmic Horror, Helm of Radiance, Rod of Asclepius, Eye
    of the Storm, Spear of Desolation, Spectral Armor, Yogi''s Necklace, Erosion,
    Jade Scepter, Pharaoh''s Curse, Chronos'' Pendant, Avenging Blade, Draconic Scale,
    Golden Blade, Obsidian Shard, Lernaean Bow, The Reaper, Damaru, Triton''s Conch,
    Leviathan''s Hide, Wish-Granting Pearl.'
  slot_scores:
    Genji's Guard:
      total: 0.51
      efficiency: 0.72
      win: 0.47
      pick: 0.19
      fit: 0.25
    Berserker's Shield:
      total: 0.51
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.26
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.42
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.5
    Gluttonous Grimoire:
      total: 0.54
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.53
    The Crusher:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.42
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
    Grimoire, Freya''s Tears, Oni Hunter''s Garb, Shifter''s Shield, Shield of the
    Phoenix, Erosion, Soul Gem, Draconic Scale, Spectral Armor, Helm of Radiance,
    Rod of Asclepius, Leviathan''s Hide, Yogi''s Necklace, Midgardian Mail, Mantle
    Of Discord, Stone of Binding, Hide of the Nemean Lion, Jade Scepter, Gladiator''s
    Shield, Screeching Gargoyle, Chronos'' Pendant, Magi''s Cloak.'
  slot_scores:
    Eye of Providence:
      total: 0.54
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.63
    Genji's Guard:
      total: 0.53
      efficiency: 0.72
      win: 0.47
      pick: 0.19
      fit: 0.39
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
      total: 0.52
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.62
    Amanita Charm:
      total: 0.55
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.63
  starter: *id001
---
